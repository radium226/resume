from dataclasses import dataclass, field
from typing import TypeAlias, Generator, Callable, Protocol, Optional
from contextlib import ExitStack, contextmanager, nullcontext
from subprocess import Popen, CompletedProcess, run, STDOUT
from enum import Enum, auto
from pathlib import Path
from tempfile import mkstemp
from time import sleep
from signal import SIGINT
import re

from .display import Display


WindowID: TypeAlias = str


class App(Protocol):

    def provide_command(self, session: "Session") -> list[str]:
        pass

    def find_window(self, session: "Session") -> Optional["Window"]:
        pass


@dataclass
class Window():

    session: "Session"
    
    id: WindowID

    @property
    def name(self) -> str:
        stdout = self.session.run(["xdotool", "getwindowname", f"{self.id}"], capture_output=True, text=True).stdout
        if isinstance(stdout, str):
            return stdout.strip()
        else:
            raise Exception("We should not be here! ")


    @property
    def props(self) -> dict[str, str]:

        def _iter_props() -> Generator[tuple[str, str], None, None]:
            stdout = self.session.run(["obxprop", "--id", f"{self.id}"], capture_output=True, text=True).stdout
            if not isinstance(stdout, str):
                raise Exception("We should not be here! ")
            lines = stdout.splitlines()
            pattern = re.compile("""^(?P<name>[A-Z_]+)\(UTF8_STRING\) = "(?P<value>.*)"$""")
            for line in lines:
                if (result := pattern.match(line)):
                    name = result.group("name")
                    value = result.group("value")
                    yield (name, value)

        return { name: value for name, value in _iter_props() }

class StopProcessCallable(Protocol):

    def __call__(self, process: Popen) -> None:
        pass


class StopProcess:

    @staticmethod
    def kill(process: Popen) -> None:
        process.kill()

    @staticmethod
    def terminate_and_wait(process: Popen) -> None:
        process.send_signal(SIGINT)
        process.wait()


@dataclass
class Session():

    display: Display = field(default_factory=Display)

    _exit_stack: ExitStack = field(default_factory=ExitStack)

    def _run_openbox(self) -> None:
        config_file_path = Path(__file__).parent / "data" / "openbox" / "rc.xml"
        self.run(
            ["openbox", "--config-file", f"{config_file_path}"],
            background=True,
            include_display_in_env=True
        )

    def __enter__(self):
        self.run(
            [
                "Xvfb", 
                f":{self.display.number}", 
                "-screen", "0", f"{self.display.size.width}x{self.display.size.height}x24",
            ],
            background=True,
            include_display_in_env=False,
        )
        sleep(2) # FIXME


        # fluxbox_folder_path = Path(__file__).parent / "data" / "fluxbox" / "init"
        # self.run(
        #     [
        #         "fluxbox",
        #         "-rc", f"{fluxbox_folder_path}",
        #         "-no-edit",
        #         "-no-toolbar"
        #     ],
        #     background=True,
        #     include_display_in_env=True,
        # )
        
        self._run_openbox()
        sleep(2) # FIXME

        return self

    def __exit__(self, type, value, traceback):
        self._exit_stack.close()


    @contextmanager
    def _run_in_background(
        self, 
        command: list[str], 
        include_display_in_env: bool = True, 
        env: dict[str, str] = {}, 
        stop_process: StopProcessCallable = StopProcess.terminate_and_wait,
        **kwargs
    ) -> Generator[Popen, None, None]:
        env = env | ( { "DISPLAY": f":{self.display.number}.0" } if include_display_in_env else {} )
        print(f"env={env} for command={command[0]}")
        process = Popen(
            command, 
            env=env,
            **kwargs,
        )
        try:
            yield process
        finally:
            stop_process(process)

    
    def _run_in_foreground(self, 
        command: list[str], 
        include_display_in_env: bool = True, 
        env: dict[str, str] = {},
        **kwargs,
    ) -> CompletedProcess:
        env = env | ( { "DISPLAY": f":{self.display.number}" } if include_display_in_env else {} )
        print(f"env={env} for command={command[0]}")
        return run(
            command, 
            env=env | ( { "DISPLAY": f":{self.display.number}" } if include_display_in_env else {} ),
            **kwargs,
        )


    def run(self, 
        command, 
        *,
        background: bool = False, 
        include_display_in_env: bool = True,
        stop_process: StopProcessCallable = StopProcess.terminate_and_wait,
        **kwargs,
    ) -> Popen | CompletedProcess:
        if background:
            return self._exit_stack.enter_context(
                self._run_in_background(
                    command, 
                    include_display_in_env=include_display_in_env, 
                    stop_process=stop_process,
                    **kwargs,
                )
            )
        else:
            return self._run_in_foreground(
                command, 
                include_display_in_env=include_display_in_env,
                **kwargs,
            )

    @property
    def windows(self) -> list[Window]:
        stdout = self.run(
            ["wmctrl", "-l"],
            background=False,
            include_display_in_env=True,
            capture_output=True,
            text=True,
        ).stdout

        if not isinstance(stdout, str):
            raise Exception("We should not be here! ")
        
        return [
            Window(self, line.split(" ")[0])
            for line in stdout.splitlines()
            if ( line or "" ).strip() != ""
        ]

    def open_app(
        self,
        app: App,
        wait_for_window: bool = True
    ) -> Window | None:
        
        self.run(app.provide_command(self), background=True)

        if wait_for_window:
            while not (window := app.find_window(self)):
                sleep(0.5)

            return window

        return None


    def take_picture(self, file_path: Path | None = None) -> Path:
        if not file_path:
            _, file_path_str = mkstemp(prefix="snapshot", suffix=".png")
            if not file_path_str:
                raise Exception("We should not be here! ")
            file_path = Path(file_path_str)

        self.run(
            ["scrot", f"{file_path}"], 
            include_display_in_env=True,
        )
        return file_path


    def record_video(self, file_path: Path | None = None) -> Path:
        if not file_path:
            _, file_path_str = mkstemp(prefix="snapshot", suffix=".mp4")
            if not file_path_str:
                raise Exception("We should not be here! ")
            file_path = Path(file_path_str)
            
        self.run(
            [
                "ffmpeg",
                "-y",
                "-hide_banner", 
                "-loglevel", "error",
                "-framerate", "25",
                "-f", "x11grab",
                "-s", f"{self.display.size.width}x{self.display.size.height}",
                "-i", f":{self.display.number}.0",
                f"{file_path}",
            ],
            include_display_in_env=False,
            background=True
        )

        return file_path
