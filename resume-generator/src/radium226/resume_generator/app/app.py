from click import group

from .parse import parse
from .generate import generate

@group()
def app():
    pass

app.add_command(parse)
app.add_command(generate)