from flask_restful import Resource
from src.app.appctx import result, data
from src.app.repository import example

class Example(Resource):
    def post(self):
        payload = data.cast_json()
        userData = {
            "id": None,
            "name": payload["name"]
        }
        try:
            response = example.insert(userData)
            userData['id']= response
        except Exception as e:
            return result.response(404, message="Eror:> "+str(e))
        else:
            return result.response(200, data=userData)

class List(Resource):
    def get(self):
        limit = int(data.cast_params('limit'))
        page = int(data.cast_params("page"))
        try:
            response = example.find(limit=limit, page=page)
        except Exception as e:
            return result.response(404, message="Eror:> "+str(e))
        else:
            return result.response(200, data=response)

class Detail(Resource):
    def get(self, id):
        try:
            response = example.fetch(id)
        except Exception as e:
            return result.response(404, message="Eror:> "+str(e))
        else:
            return result.response(200, data=response)

class Delete(Resource):
    def delete(self, id):
        try:
            example.delete(id)
        except Exception as e:
            return result.response(404, message="Eror:> "+str(e))
        else:
            return result.response(200, message="Delete data successfuly")