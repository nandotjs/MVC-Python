from flask import Blueprint, jsonify
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pet_lister_composer import list_all_pets_composer
from src.main.composer.pet_deleter_composer import delete_pet_composer

pets_routes_bp = Blueprint('pets_routes', __name__)

@pets_routes_bp.route('/pets', methods=['GET'])
def list_all():
    http_request = HttpRequest()
    view = list_all_pets_composer()
    http_response = view.render(http_request)
    return jsonify(http_response.body), http_response.status_code

@pets_routes_bp.route('/pets/<int:pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    http_request = HttpRequest(params={'pet_id': pet_id})
    view = delete_pet_composer()
    http_response = view.render(http_request)
    return jsonify(http_response.body), http_response.status_code
