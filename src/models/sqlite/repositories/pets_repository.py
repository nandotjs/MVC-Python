from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import Pets

class PetsRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create(self, pet: Pets) -> Pets:
        with self.db_connection as database:
            try:
                database.session.add(pet)
                database.session.commit()
                return pet
            except Exception as e:
                database.session.rollback()
                raise e

    def list_all(self) -> list:
        with self.db_connection as database:
            try:
                pets = database.session.query(Pets).all()
                return pets
            except NoResultFound:
                return []

    def delete(self, pet_id: int) -> None:
        with self.db_connection as database:
            try:
                database.session.query(Pets).filter(Pets.id == pet_id).delete()
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
