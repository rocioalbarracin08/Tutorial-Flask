import sqlite3
from datetime import datetime

import click
from flask import current_app, g #Objeto especial/ Único para cada solicitud. Almacena datos a los que podrían acceder VARIAS funciones (durante la petición)


def get_db(): #La conexión se almacena y se reutiliza en lugar de crear una nueva conexión si se llama a get_db por segunda vez en la misma petición
    if 'db' not in g:
        g.db = sqlite3.connect( #establece una conexión con el fichero apuntado por la clave de configuración DATABASE - existe a partir de inicializar la base de datos.
            current_app.config['DATABASE'], #Objeto especial/ Maneja la solicitud
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)