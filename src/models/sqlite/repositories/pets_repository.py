from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import Pets

class PetsRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def list_all(self) -> list:
        with self.db_connection as database:
            try:
                pets = database.session.query(Pets).all()
                return pets
            except NoResultFound:
                return []
