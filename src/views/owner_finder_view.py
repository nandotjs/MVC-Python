from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.owner_finder_controller_interface import OwnerFinderControllerInterface

class OwnerFinderView(ViewInterface):
    def __init__(self, owner_finder_controller: OwnerFinderControllerInterface) -> None:
        self.owner_finder_controller = owner_finder_controller

    def render(self, http_request: HttpRequest) -> HttpResponse:
        owner_id = http_request.params["owner_id"]
        owner_info = self.owner_finder_controller.find(owner_id)
        return HttpResponse(200, owner_info) 