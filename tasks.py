import os

from pathlib import Path

from invoke import task, Context  # type: ignore

CURRENT_DIRECTORY = Path(__file__).resolve()

MAIN_DIRECTORY_PATH = Path(__file__).parent

# If no version is indicated, we will take the latest
VERSION = os.getenv("INFRAHUB_VERSION", None)
COMPOSE_COMMAND = f"curl https://infrahub.opsmill.io/{VERSION if VERSION else ''} | docker compose -f -"
COMPOSE_COMMAND_LOCAL = "docker compose"


def has_local_docker_file() -> bool:
    file_path = Path(MAIN_DIRECTORY_PATH, "docker-compose.yml")
    return file_path.is_file()


def get_docker_command() -> str:
    if has_local_docker_file():
        return COMPOSE_COMMAND_LOCAL
    return COMPOSE_COMMAND


@task
def start(context: Context) -> None:
    with context.cd(MAIN_DIRECTORY_PATH):
        context.run(f"{get_docker_command()} up -d")


@task
def load_schema(context: Context) -> None:
    context.run("infrahubctl schema load schemas/**/*.yml --wait 30")
    context.run("infrahubctl menu load menus/base_menu.yml")


@task
def load_data(context: Context) -> None:
    context.run("infrahubctl object load objects/groups.yml")
    context.run("infrahubctl object load objects/organizations/**")

    context.run("infrahubctl object load objects/locations/countries.yml")
    context.run("infrahubctl object load objects/locations/sites.yml")
    context.run("infrahubctl object load objects/locations/suites.yml")
    context.run("infrahubctl object load objects/locations/racks.yml")

    context.run("infrahubctl object load objects/dcim/platforms.yml")
    context.run("infrahubctl object load objects/dcim/device_types.yml")

    context.run("infrahubctl object load objects/dcim/ip_prefixes.yml")
    context.run("infrahubctl object load objects/dcim/interface_ips.yml")

    context.run("infrahubctl object load objects/dcim/devices.yml")
    context.run("infrahubctl object load objects/dcim/interfaces.yml")


    # context.run("infrahubctl object load objects/dcim/cables.yml")

@task
def destroy(context: Context) -> None:
    with context.cd(MAIN_DIRECTORY_PATH):
        context.run(f"{get_docker_command()} down -v")


@task
def stop(context: Context) -> None:
    with context.cd(MAIN_DIRECTORY_PATH):
        context.run(f"{get_docker_command()} down")


@task
def restart(context: Context, component: str = "") -> None:
    with context.cd(MAIN_DIRECTORY_PATH):
        if component:
            context.run(f"{get_docker_command()} restart {component}")
            return

        context.run(f"{get_docker_command()} restart")
