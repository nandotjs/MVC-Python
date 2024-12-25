from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection
from src.main.routes.pets_routes import pets_routes_bp
from src.main.routes.owners_routes import owners_routes_bp

db_connection.connect()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pets_routes_bp)
app.register_blueprint(owners_routes_bp)
