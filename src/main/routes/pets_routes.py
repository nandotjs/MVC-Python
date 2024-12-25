from flask import Blueprint

pets_routes_bp = Blueprint('pets_routes', __name__)

@pets_routes_bp.route('/pets', methods=['GET'])
def list_all():
    return 'Hello, World!'
