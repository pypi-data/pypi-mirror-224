import typer

app = typer.Typer()


def ai_example():
    typer.echo("Running AI")


@app.command()
def ai():
    ai_example()
