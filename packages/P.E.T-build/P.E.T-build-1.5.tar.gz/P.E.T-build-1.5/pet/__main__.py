import typer
from .gps import app as gps

app = typer.Typer()

app.add_typer(gps, name='gps')

app()