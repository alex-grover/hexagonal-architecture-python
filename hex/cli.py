import subprocess
from typing import Union

import click
from dotenv import load_dotenv


def validate_env(_context: click.Context, _parameter: Union[click.Option, click.Parameter],
                 env: str) -> str:
    values = ('dev', 'test')
    if env not in values:
        raise click.BadParameter(f'`env` must be one of: {values}')

    return env


@click.group('Hex server CLI')
def cli() -> None:
    pass


@cli.command(help='Run the web server')
def server() -> int:
    return subprocess.call(['flask', 'run'])


@cli.group(help="Manage the database")
def db() -> None:
    pass


@db.command(help="Create the database")
@click.argument('env', envvar='ENV', default='dev', callback=validate_env)
def create(env: str) -> int:
    click.echo(f'Creating database for `{env}` environment...')

    db_name = f'hex_{env}'
    return subprocess.call(['createdb', db_name])


@db.command(help="Run the database migrations")
@click.argument('env', envvar='ENV', default='dev', callback=validate_env)
def migrate(env: str) -> int:
    click.echo(f'Running migrations for `{env}` environment...')

    dotenv_file = '.env'
    if env != 'dev':
        dotenv_file = f'.env.{env}'

    load_dotenv(dotenv_file)

    return subprocess.call(['alembic', 'upgrade', 'head'])


@cli.group(help='Run the code quality tools')
def check() -> None:
    pass


@check.command(help='Run the linter')
def style() -> int:
    click.echo('Running `flake8`...')
    return subprocess.call('flake8')


@check.command(help='Run the test suite')
def tests() -> int:
    click.echo('Running `pytest`...')
    return subprocess.call('pytest')


@check.command(help='Run the static analyzer')
def types() -> int:
    click.echo('Running `mypy`...')
    return subprocess.call('mypy')
