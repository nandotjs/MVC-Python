from src.models.sqlite.entities.owners import Owners

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
