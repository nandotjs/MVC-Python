from sqlalchemy import Engine
from .connection import db_connection
import pytest

@pytest.mark.skip(reason="DB integration test")
def test_connection():
    db_connection.connect()
    engine = db_connection.get_engine()
    assert engine is not None
    assert isinstance(engine, Engine)
