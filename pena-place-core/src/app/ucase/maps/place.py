from flask_restful import Resource, reqparse, fields
from src.app.appctx import result, data
from src.pkg import gmaps
import datetime


class MapsPlaces(Resource):   
    def post(self):
        payload = data.cast()
        try:
            maps_driver = gmaps.setup_maps("https://www.google.com/maps")
            gmaps.maximize_window(maps_driver)
            gmaps.search_place(maps_driver, payload["keyword"], payload["no_use_category"])
        except Exception:
            return result.response(204, message="Search stopped by action")
        else:
            return result.response(200, message="grabs data")


