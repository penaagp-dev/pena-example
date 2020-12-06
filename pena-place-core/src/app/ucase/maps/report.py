from flask_restful import Resource, reqparse, fields
from src.app.appctx import result, data
from src.consts.path import APP_ROOT
import csv

class MapsPlacesStatus(Resource):   
    def get(self, id):
        path_result = APP_ROOT+"/log"
        file_result = path_result+"/_"+id+".csv"
        response = []
        try:
            with open(file_result, encoding='utf-8') as csvf: 
                csvReader = csv.DictReader(csvf) 
                for i in csvReader:
                    response.append(i)
        except Exception:
            return result.response(500, "Internal Failure")
        else:
            return result.response(200, "grabs data report", response)
