from src.models.sqlite.settings.connection import db_connection
from src.models.sqlite.repositories.owners_repository import OwnersRepository
from src.controllers.owner_finder_controller import OwnerFinderController
from src.views.owner_finder_view import OwnerFinderView

def find_owner_composer():
    model = OwnersRepository(db_connection)
    controller = OwnerFinderController(model)
    view = OwnerFinderView(controller)
    return view
