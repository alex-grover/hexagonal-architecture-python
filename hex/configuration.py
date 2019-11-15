import os

import inject
from flask import Flask

from hex.adapters.database.postgres import PostgresAdapter
from hex.domain.database_interface import DatabaseInterface


def configure_application(application: Flask) -> None:
    application.config.update(
        DATABASE_URI=os.getenv('DATABASE_URI')
    )


def configure_inject(application: Flask) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(DatabaseInterface, PostgresAdapter(application.config['DATABASE_URI']))

    inject.configure(config)
