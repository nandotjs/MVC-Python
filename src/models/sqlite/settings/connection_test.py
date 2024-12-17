from sqlalchemy import Engine
from .connection import db_connection

def test_connection():
    engine = db_connection.get_engine()
    assert engine is None
    db_connection.connect()
    engine = db_connection.get_engine()
    assert engine is not None
    assert isinstance(engine, Engine)
