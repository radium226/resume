from dataclasses import dataclass, field
from typing import TypeAlias, Generator, Callable, Protocol
from contextlib import ExitStack, contextmanager, nullcontext
from subprocess import Popen, CompletedProcess, run, STDOUT
from enum import Enum, auto
from pathlib import Path
from tempfile import mkstemp
from time import sleep
from signal import SIGINT

from .display import Display


WindowID: TypeAlias = str


@dataclass
class Window():

    session: "Session"
    
    id: WindowID
    

    def maximize(self) -> None: # FIXME
        command=["wmctrl", "-r", f"{self.id}", "-b", "remove,maximized_vert,maximized_horz"]
        self.session.run(command, background=False)

    def minimize(self) -> None: # FIXME
        self.session.run(["xdotool", "windowminimize", f"{self.id}"], background=False)


class StopProcess(Protocol):

    @staticmethod
    def kill(process: Popen) -> None:
        process.kill()

    def terminate_and_wait(process: Popen) -> None:
        process.send_signal(SIGINT)
        process.wait()

    def __call__(self, process: Popen) -> None:
        pass


@dataclass
class Session():

    display: Display = field(default_factory=Display)

    _exit_stack: ExitStack = field(default_factory=ExitStack)

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

        self.run(
            [
                "fluxbox",
                "-no-slit",
                "-no-toolbar",
            ],
            background=True,
            include_display_in_env=True,
        )
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
        stop_process: StopProcess = StopProcess.terminate_and_wait,
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
        stop_process: StopProcess = StopProcess.terminate_and_wait,
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


    def open(
        self,
        command: list[str],
    ) -> "Window":
        process = self.run(command, background=True)

        sleep(5)

        window_id = [
            line.split(" ")[0]
            for line in self.run(
                ["wmctrl", "-l"], # FIXME
                background=False,
                include_display_in_env=True,
                capture_output=True,
                text=True,
            ).stdout.split("\n")
        ][0]
        
        return Window(self, window_id)


    def take_picture(self, file_path: Path | None = None) -> Path:
        if not file_path:
            _, file_path = mkstemp(prefix="snapshot", suffix=".png")

        self.run(
            ["scrot", f"{file_path}"], 
            include_display_in_env=True,
        )
        return file_path


    def record_video(self, file_path: Path | None = None) -> Path:
        if not file_path:
            _, file_path = mkstemp(prefix="snapshot", suffix=".mp4")

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
