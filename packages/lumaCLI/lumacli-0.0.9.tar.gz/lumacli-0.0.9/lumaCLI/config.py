import typer
from lumaCLI.models import Config
from rich import print
from pathlib import Path
from lumaCLI.utils import get_config, send_config
from lumaCLI.common import LumaURL, ConfigDir

app = typer.Typer(
    name="config", no_args_is_help=True, pretty_exceptions_show_locals=False
)


@app.command(help="Display the current configuration information.")
def show(config_dir: Path = ConfigDir):
    """
    This function retrieves and prints the current configuration information.
    """
    config: Config = get_config(config_dir=config_dir)
    print(config)
    raise typer.Exit(0)


@app.command(help="Send the current configuration information to luma")
def send(config_dir: Path = ConfigDir, luma_url: str = LumaURL):
    """
    This function sends the current configuration information to the specified endpoint.
    """
    # Retrieve the global config object
    config: Config = get_config(config_dir=config_dir)

    # Send the configuration and exit the program
    response = send_config(config=config, luma_url=luma_url)
    if not response.ok:
        raise typer.Exit(1)
