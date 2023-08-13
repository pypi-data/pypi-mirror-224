import typer


app = typer.Typer(no_args_is_help=True)


@app.callback()
def callback():
    """
    dkdc
    """


@app.command()
def run():
    """
    Run
    """
    typer.echo("running...")


@app.command()
def ai():
    """
    AI
    """
    typer.echo("AIing...")


def main():
    app()


if __name__ == "__main__":
    main()
