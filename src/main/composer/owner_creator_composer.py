from src.models.sqlite.settings.connection import db_connection
from src.models.sqlite.repositories.owners_repository import OwnersRepository
from src.controllers.owner_creator_controller import OwnerCreatorController
from src.views.owner_creator_view import OwnerCreatorView

def create_owner_composer():
    model = OwnersRepository(db_connection)
    controller = OwnerCreatorController(model)
    view = OwnerCreatorView(controller)
    return view
