from flask_restful import Resource, reqparse, fields
from src.app.appctx import result, data
from src.consts.path import APP_ROOT
from src.app.libs import thread
from src.pkg.utils import file
import csv

import datetime


class MapsPlaces(Resource):   
    def post(self):
        payload = data.cast()
        
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        path_result = APP_ROOT+"/log"
        file.makedirs(path_result)
        file_result = "/log/_"+suffix+".csv"
        try:
            thread.GmapsThreading(payload, path_result, suffix)
        except Exception:
            # with open(file_result, encoding='utf-8') as csvf: 
            #     csvReader = csv.DictReader(csvf) 
            #     for i in csvReader:
            #         response.append(i)
            return result.response(501, "Error")
        else:
            response = {
                "id": suffix,
                "path": file_result
            }
            return result.response(200, "Processing Grab: Dont close your maps", response)


