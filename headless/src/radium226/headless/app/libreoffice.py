from dataclasses import dataclass
from pathlib import Path

from ..session import App, Window, Session


@dataclass
class LibreOffice(App):

    file_path: Path | None = None

    def provide_command(self, session: Session) -> list[str]:
        return ["soffice", "--norestore"] + ([f"{self.file_path}"] if self.file_path else [] )

    def find_window(self, session: Session) -> Window | None:
        for window in session.windows:
            if self.file_path:
                if self.file_path.name in window.props.get("_NET_WM_VISIBLE_NAME"):
                    return window
            else:
                if window.props.get("_OB_APP_CLASS", None) == "libreoffice-startcenter":
                    return window

        return None