from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.main.composer.owner_creator_composer import create_owner_composer

owners_routes_bp = Blueprint('owners_routes', __name__)

@owners_routes_bp.route('/owners', methods=['POST'])
def create_owner():
    http_request = HttpRequest(body=request.json)
    view = create_owner_composer()
    http_response = view.render(http_request)
    return jsonify(http_response.body), http_response.status_code
