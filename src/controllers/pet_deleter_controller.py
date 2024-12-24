from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface

class PetDeleterController:
    def __init__(self, pets_repository: PetsRepositoryInterface):
        self.pets_repository = pets_repository

    def delete(self, pet_id: int) -> None:
        try:
            self.__delete_pet_from_db(pet_id)
            return self.__format_response()
        except Exception as e:
            return self.__format_error_response(str(e))

    def __delete_pet_from_db(self, pet_id: int) -> None:
        self.pets_repository.delete(pet_id)

    def __format_response(self) -> dict:
        return {
            "data": {
                "type": "pet",
                "message": "Pet deleted successfully"
            }
        }

    def __format_error_response(self, error_message: str) -> dict:
        return {
            "errors": [{
                "status": "400",
                "title": "Delete Failed",
                "detail": error_message
            }]
        } 