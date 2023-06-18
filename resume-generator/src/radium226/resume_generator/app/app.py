from click import group

from .parse import parse

@group()
def app():
    pass

app.add_command(parse)