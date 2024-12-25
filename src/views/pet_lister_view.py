from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.pet_lister_controller_interface import PetListerControllerInterface

class PetListerView(ViewInterface):
    def __init__(self, pet_lister_controller: PetListerControllerInterface) -> None:
        self.pet_lister_controller = pet_lister_controller

    def render(self, http_request: HttpRequest) -> HttpResponse:
        pets = self.pet_lister_controller.list()
        return HttpResponse(200, pets) 