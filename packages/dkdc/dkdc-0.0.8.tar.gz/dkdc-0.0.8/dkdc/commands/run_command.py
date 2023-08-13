import typer

app = typer.Typer()


def run_example():
    typer.echo("Running the example")


@app.command()
def run():
    run_example()
