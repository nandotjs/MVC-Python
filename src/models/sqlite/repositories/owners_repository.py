from src.models.sqlite.entities.owners import Owners
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import Pets

class OwnersRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        with self.db_connection as database:
            try:
                owner = Owners(first_name=first_name, last_name=last_name, age=age, pet_id=pet_id)
                database.session.add(owner)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
            
    def get_owner_by_id(self, id: int) -> Owners:
        with self.db_connection as database:
            try:
                owner = (
                    database.session
                        .query(Owners)
                        .outerjoin(Pets, Pets.id == Owners.pet_id)
                        .filter(Owners.id == id)
                        .with_entities(
                            Owners.first_name,
                            Owners.last_name,
                            Pets.name.label("pet_name"),
                            Pets.type.label("pet_type")
                        ) 
                        .one()
                )
                return owner
            except NoResultFound:
                return None

