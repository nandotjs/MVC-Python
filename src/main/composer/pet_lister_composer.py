from src.models.sqlite.settings.connection import db_connection
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.controllers.pet_lister_controller import PetListerController
from src.views.pet_lister_view import PetListerView

def list_all_pets_composer():
    model = PetsRepository(db_connection)
    controller = PetListerController(model)
    view = PetListerView(controller)
    return view
