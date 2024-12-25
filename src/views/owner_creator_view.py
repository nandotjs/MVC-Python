from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.owner_creator_controller_interface import OwnerCreatorControllerInterface

class OwnerCreatorView(ViewInterface):
    def __init__(self, owner_creator_controller: OwnerCreatorControllerInterface) -> None:
        self.owner_creator_controller = owner_creator_controller

    def render(self, http_request: HttpRequest) -> HttpResponse:
        owner_info = self.owner_creator_controller.create(http_request.body)
        return HttpResponse(201, owner_info)

