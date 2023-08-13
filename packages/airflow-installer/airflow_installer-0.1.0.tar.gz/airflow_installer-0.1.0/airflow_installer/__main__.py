import os
import shutil
import subprocess
import sys
import venv

import httpx
import typer
from rich import print

app = typer.Typer()


def is_airflow_installed(venv_path: str, version: str) -> bool:
    venv_bin_python = os.path.join(venv_path, "bin", "python")
    if not os.path.exists(venv_bin_python):
        return False

    try:
        subprocess.run([venv_bin_python, "-m", "airflow", "version"], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False


def install_airflow(
    version: str,
    venv_path: str,
    constraints_url: str,
    extras: str = "",
    requirements: str = "",
    verbose: bool = False,
):
    if is_airflow_installed(venv_path, version):
        print(
            f"[bold yellow]Apache Airflow {version} is already installed. Skipping installation.[/bold yellow]"
        )
        return

    venv_bin_python = os.path.join(venv_path, "bin", "python")
    if not os.path.exists(venv_bin_python):
        print(f"[bold red]Virtual environment at {venv_path} does not exist or is not valid.[/bold red]")
        raise SystemExit()

    upgrade_pipeline_command = f"{venv_bin_python} -m pip install --upgrade pip setuptools wheel"

    install_command = f"{upgrade_pipeline_command} && {venv_bin_python} -m pip install 'apache-airflow=={version}{extras}' --constraint {constraints_url}"

    if requirements:
        install_command += f" -r {requirements}"

    try:
        if verbose:
            print(f"Running command: [bold]{install_command}[/bold]")
        subprocess.run(install_command, shell=True, check=True)
        print(f"[bold green]Apache Airflow {version} installed successfully![/bold green]")
        print(f"Virtual environment at {venv_path}")
    except subprocess.CalledProcessError:
        print("[bold red]Error occurred during installation.[/bold red]")
        raise SystemExit()


def get_latest_airflow_version(verbose: bool = False) -> str:
    try:
        with httpx.Client() as client:
            response = client.get("https://pypi.org/pypi/apache-airflow/json")
            data = response.json()
            latest_version = data["info"]["version"]
            if verbose:
                print(f"Latest Apache Airflow version detected: [bold cyan]{latest_version}[/bold cyan]")
            return latest_version
    except (httpx.RequestError, KeyError) as e:
        if verbose:
            print(f"[bold red]Error occurred while retrieving latest version: {e}[/bold red]")
            print("[bold yellow]Defaulting to Apache Airflow version 2.7.0[/bold yellow]")
        return "2.7.0"


def verify_or_create_venv(venv_path: str, recreate: bool):
    venv_path = os.path.abspath(venv_path)

    if recreate and os.path.exists(venv_path):
        print(f"Recreating virtual environment at [bold blue]{venv_path}[/bold blue]")
        shutil.rmtree(venv_path)

    if not os.path.exists(venv_path):
        venv.create(venv_path, with_pip=True)
        print(f"Virtual environment created at [bold blue]{venv_path}[/bold blue]")

    return venv_path


def print_next_steps(venv_path, version):
    activated_venv_path = os.environ.get("VIRTUAL_ENV")

    next_steps = """
    Next Steps:
    """

    activate_command = f"$ source {venv_path}/bin/activate"

    need_to_activate = not activated_venv_path or activated_venv_path != os.path.dirname(venv_path)
    if need_to_activate:
        next_steps += f"""
    1. Activate the virtual environment:
       [bold blue]{activate_command}[/bold blue]
    """

    next_steps += f"""
    {2 if need_to_activate else 1}. Run Apache Airflow in standalone mode using the following command:
       [bold blue]$ airflow standalone[/bold blue]

    {3 if need_to_activate else 2}. Access the Airflow UI in your web browser at: [bold cyan]http://localhost:8080[/bold cyan]

    For more information and guidance, please refer to the Apache Airflow documentation:
    [bold cyan]https://airflow.apache.org/docs/apache-airflow/{version}/[/bold cyan]
    """

    print(next_steps)


@app.command()
def main(
    version: str = typer.Option(
        default=get_latest_airflow_version(),
        help="Apache Airflow version to install. Defaults to latest.",
    ),
    constraints_url: str = typer.Option(
        default=None,
        help="URL of the constraints file. Defaults to latest version constraints.",
        show_default=False,
    ),
    extras: str = typer.Option(
        "",
        help="Extras or additional requirements to install with Apache Airflow.",
    ),
    requirements: str = typer.Option(
        "",
        help="Path to a requirements.txt file to be used during installation.",
    ),
    venv_path: str = typer.Option(
        default=".venv/airflow",
        help="Path where the virtual environment will be created",
    ),
    recreate_venv: bool = typer.Option(
        False,
        help="Recreate virtual environment if it already exists.",
    ),
    verbose: bool = typer.Option(
        False,
        help="Enable verbose debugging output.",
    ),
):
    print(f"Installing Apache Airflow in virtual environment at [bold blue]{venv_path}[/bold blue]")

    venv_path = verify_or_create_venv(venv_path, recreate_venv)

    # Determine the Python version in the virtual environment
    venv_python_version = f"{sys.version_info.major}.{sys.version_info.minor}"

    constraints_url = (
        constraints_url
        or f"https://raw.githubusercontent.com/apache/airflow/constraints-{version}/constraints-{venv_python_version}.txt"
    )

    install_airflow(version, venv_path, constraints_url, extras, requirements, verbose)
    print_next_steps(venv_path, version)


if __name__ == "__main__":
    app()
