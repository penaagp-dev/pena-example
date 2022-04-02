from unicodedata import name
from flask_restful import Resource, reqparse, fields
from src.app.appctx import result, data
from src.app.repository import user
import datetime

class User(Resource):
    def post(self):
        payload = data.cast_json()
        userData = {
                "id" : None,
                "name": payload['name']
            }
        try:
            id = user.insert(userData)
            userData['id']= id
        except Exception as e:
            return result.response(404, message="Error:> "+str(e))
        else:
            return result.response(200, data=userData)
    def get(self):
        limit  = int(data.cast_params('limit'))
        page  = int(data.cast_params('page'))
        list = user.find(limit=limit, page=page)
        return result.response(200, data=list)