from typing import Generator
from subprocess import run, Popen
from contextlib import contextmanager
from dataclasses import dataclass
import os

# https://github.com/radium226/encheres-publiques/blob/master/src/main/scala/com/github/radium226/browsing/Display.scala


@contextmanager
def run_in_background(command: list[str], env: dict[str, str] = {}) -> Generator[Popen, None, None]:
    process = Popen(command, env=env)
    try:
        yield process
    finally:
        process.kill()


@dataclass
class Size():

    width: int

    height: int


@dataclass
class Display():

    number: int

    def run(self, command: list[str]) -> None:
        env = os.environ.copy()
        env["DISPLAY"] = ":{self.number}.0"
        run(command, env)



@contextmanager
def display(number: int = 6, size = Size(800, 600)) -> Generator[Display, None, None]:
    xvfb_command=[
        "Xvfb", 
        f":{number}", 
        "-screen", "0", f"{size.width}x{size.height}x24"
    ]
    with run_in_background(xvfb_command):
        ffmpeg_command = [
            "ffmpeg",
            "-y",
            "-framerate", "25",
            "-f", "x11grab",
            "-s", f"{size.width}x{size.height}",
            "-i", f":{number}.0",
            "/tmp/record.mpg"
        ]

        with run_in_background(ffmpeg_command):
            yield Display(number)