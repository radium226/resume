from headless import run_in_background, display

from time import sleep


def test_run_in_background():

    with run_in_background(command=["bash", "-c", "while sleep 1; do echo 'Bip! '; done"]):
        sleep(5)


def test_display():

    with display() as d:
        with run_in_background(["soffice"], env={
            "DISPLAY": f":{d.number}.0"
        }):
            sleep(5)