from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.pet_deleter_controller_interface import PetDeleterControllerInterface

class PetDeleterView(ViewInterface):
    def __init__(self, pet_deleter_controller: PetDeleterControllerInterface) -> None:
        self.pet_deleter_controller = pet_deleter_controller

    def render(self, http_request: HttpRequest) -> HttpResponse:
        pet_id = http_request.params["pet_id"]
        self.pet_deleter_controller.delete(pet_id)
        return HttpResponse(204, {}) 