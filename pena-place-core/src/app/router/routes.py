from flask import Blueprint
from flask_restful import Api
from src.app.ucase.health import HealthController
from src.app.ucase.maps import place, report

v1_blueprint = Blueprint("api", __name__, url_prefix='/v1')
api = Api(v1_blueprint)
api.add_resource(HealthController, '/health')
api.add_resource(place.MapsPlaces, '/place')
api.add_resource(report.MapsPlacesStatus, '/place/report/<id>')

