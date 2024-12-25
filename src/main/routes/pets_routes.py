from flask import Blueprint, jsonify
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pet_lister_composer import list_all_pets_composer

pets_routes_bp = Blueprint('pets_routes', __name__)

@pets_routes_bp.route('/pets', methods=['GET'])
def list_all():
    http_request = HttpRequest()
    view = list_all_pets_composer()
    http_response = view.render(http_request)
    return jsonify(http_response.body), http_response.status_code
