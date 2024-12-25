from src.models.sqlite.settings.connection import db_connection
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.controllers.pet_deleter_controller import PetDeleterController
from src.views.pet_deleter_view import PetDeleterView

def delete_pet_composer():
    model = PetsRepository(db_connection)
    controller = PetDeleterController(model)
    view = PetDeleterView(controller)
    return view
