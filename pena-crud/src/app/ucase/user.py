from flask_restful import Resource
from src.app.appctx import result, data
from src.app.repository import user

class Insert(Resource):
    def post(self):
        payload = data.cast_json()
        userData = {
                "name": payload['name']
            }
        try:
            id = user.insert(userData)
            userData['id']= id
        except Exception as e:
            return result.response(404, message="Error:> "+str(e))
        else:
            return result.response(200, data=userData)

class List(Resource):
    def get(self):
        limit  = int(data.cast_params('limit'))
        page  = int(data.cast_params('page'))
        
        try:
            list = user.find(limit=limit, page=page)
        except Exception as e:
            return result.response(404, message="Error:> "+str(e))
        else:
            return result.response(200, data=list)   

class Detail(Resource):
    def get(self, id):
        try:
            detail = user.fecth(id)
        except Exception as e:
            return result.response(404, message="Error:> "+str(e))
        else:
            return result.response(200, data=detail)  
            
class Update(Resource):
    def put(self, id):
        pass

class Delete(Resource):
    def delete(self, id):
        try:
            user.delete(id)
        except Exception as e:
            return result.response(404, message="Error:> "+str(e))
        else:
            return result.response(200, message="Delete successfully")