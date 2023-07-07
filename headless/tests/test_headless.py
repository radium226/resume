from radium226.headless import Session
from time import sleep
from pathlib import Path


def test_session():
    with Session() as session:
        # Record a video... 
        session.record_video(Path("/tmp/session.mp4"))
        sleep(1)

        # Run a program... 
        window = session.open(["soffice"])
        print(window)
        sleep(2.5)        