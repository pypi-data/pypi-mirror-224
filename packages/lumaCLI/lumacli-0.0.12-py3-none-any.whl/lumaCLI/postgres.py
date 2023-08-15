import typer
from typing import Dict, List

from rich import print

from lumaCLI.models import Config, RequestInfo
from lumaCLI.utils import (
    get_db_metadata,
    get_config,
    send_config,
    send_request_info,
)
from lumaCLI.common import (
    LumaURL,
    DryRun,
    NoConfig,
    PostgresUsername,
    PostgresDatabase,
    PostgresHost,
    PostgresPort,
    PostgresPassword,
)

app = typer.Typer(no_args_is_help=True, pretty_exceptions_show_locals=False)


@app.command()
def ingest(
    luma_url: str = LumaURL,
    username: str = PostgresUsername,
    database: str = PostgresDatabase,
    host: str = PostgresHost,
    port: str = PostgresPort,
    password: str = PostgresPassword,
    dry_run: bool = DryRun,
    no_config: bool = NoConfig,
) -> RequestInfo:
    """
    Sends metadata from a PostgreSQL database to a Luma ingestion endpoint.
    If 'endpoint' is not specified, it will auto-generate from the '.luma/config.yaml' file.
    """

    # get_config
    config: Config = get_config()
    should_send_config = not no_config

    # Retrieve database metadata
    db_metadata: Dict[str, List[Dict]] = get_db_metadata(
        username=username, database=database, host=host, port=port, password=password
    )

    # In dry run mode, print the database metadata and exit
    if dry_run:
        print(db_metadata)
        raise typer.Exit(0)

    endpoint = f"{luma_url}/api/v1/postgres"

    # Create the request info object to return
    request_info = RequestInfo(
        url=endpoint,
        method="POST",
        payload=db_metadata,
        verify=False,
        timeout=(3.05, 60 * 30),
    )
    if config and should_send_config:
        config_response = send_config(config=config, luma_url=luma_url)

    response = send_request_info(request_info)
    if not response.ok:
        raise typer.Exit(1)

    return response


if __name__ == "__main__":
    app()
