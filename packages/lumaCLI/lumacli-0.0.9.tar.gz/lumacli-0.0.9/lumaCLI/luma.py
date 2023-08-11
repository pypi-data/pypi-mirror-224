#!/usr/bin/env python

# Required imports
import typer
import urllib3

# Local module imports
import lumaCLI.config as config_module
import lumaCLI.dbt as dbt_module
import lumaCLI.postgres as postgres_module

from lumaCLI.common import CLI_NAME

# Disabling warnings related to insecure requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create a Typer application with set properties
app = typer.Typer(
    name=CLI_NAME,  # Set the name of the CLI
    no_args_is_help=True,  # Show help message if no arguments are provided
    pretty_exceptions_show_locals=False,  # Do not display local variables when an exception occurs
)

# Add commands to the application
app.add_typer(dbt_module.app, name="dbt")
app.add_typer(postgres_module.app, name="postgres")
app.add_typer(config_module.app, name="config")


def cli():
    """
    Entry point for the CLI.
    Used for python script installation purposes (flit).
    """
    app()


if __name__ == "__main__":
    # Entry point for the CLI.
    app()
