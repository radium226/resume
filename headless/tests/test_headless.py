from radium226.headless import Session, App, Window
from time import sleep
from pathlib import Path


class LibreOffice(App):

    def provide_command(self, session: Session) -> list[str]:
        return ["soffice"]

    def find_window(self, session: Session) -> Window | None:
        for window in session.windows:
            print(window)
            if window.name.lower() == "libreoffice":
                return window

        return None


def test_session():
    with Session() as session:
        # Record a video... 
        session.record_video(Path("/tmp/session.mp4"))
        sleep(1)

        # Run a program... 
        libreoffce_window = session.open_app(LibreOffice(), wait_for_window=True)
        print(libreoffce_window)
        sleep(2.5)