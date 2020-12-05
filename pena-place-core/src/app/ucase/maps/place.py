from flask_restful import Resource, reqparse, fields
from src.app.appctx import result, data
from src.pkg import gmaps
from src.consts.path import APP_ROOT
import csv

import datetime


class MapsPlaces(Resource):   
    def post(self):
        payload = data.cast()
        response = []
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        path_result = APP_ROOT+"/log"
        file_result = path_result+"/_"+suffix+".csv"
        try:
            maps_driver = gmaps.setup_maps("https://www.google.com/maps")
            gmaps.maximize_window(maps_driver)
            response = gmaps.search_place(maps_driver, payload["keyword"], payload["no_use_category"], path_result, suffix)
        except Exception:
            with open(file_result, encoding='utf-8') as csvf: 
                csvReader = csv.DictReader(csvf) 
                for i in csvReader:
                    response.append(i)
            return result.response(499, "Canceled Operation", response)
        else:
            with open(file_result, encoding='utf-8') as csvf: 
                csvReader = csv.DictReader(csvf) 
                for i in csvReader:
                    response.append(i)
            return result.response(200, "grabs data", response)


