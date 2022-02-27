"""Criaçao de bancos de dados SQLite"""
from my_starwars.config import CONNECTION_STRING
from my_starwars.infra.database.entities import *  # pylint: disable=W0401, W0614
from . import DataBaseConnectionHandler, Base


def create_database(connection_string: str = CONNECTION_STRING):
    """Criaçao de banco de dados SQLite"""

    db_connection = DataBaseConnectionHandler(connection_string)
    engine = db_connection.get_engine()
    base = Base.metadata.create_all(engine)

    return base
