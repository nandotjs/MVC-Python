from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.main.composer.owner_creator_composer import create_owner_composer
from src.main.composer.owner_finder_composer import find_owner_composer
from src.errors.error_handler import handle_error

owners_routes_bp = Blueprint('owners_routes', __name__)

@owners_routes_bp.route('/owners', methods=['POST'])
def create_owner():
    try:
        http_request = HttpRequest(body=request.json)
        view = create_owner_composer()
        http_response = view.render(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        http_response = handle_error(e)
        return jsonify(http_response.body), http_response.status_code

@owners_routes_bp.route('/owners/<int:owner_id>', methods=['GET'])
def find_owner(owner_id):
    try:
        http_request = HttpRequest(params={'owner_id': owner_id})
        view = find_owner_composer()
        http_response = view.render(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        http_response = handle_error(e)
        return jsonify(http_response.body), http_response.status_code

