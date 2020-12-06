from flask_restful import Resource, reqparse, fields, request
from src.app.appctx import result, data
from src.app.repositories import category_grup
import datetime


class CategroyGrup(Resource):   
    def post(self):
        payload = data.cast()
        try:
            id = category_grup.upsert(payload)
        except Exception:
            return result.response(500, "Internal Failure")
        else:
            payload["id"] = id
            return result.response(200, "category grup", payload)

    def get(self):
        limit = request.args.get("limit")
        offset = request.args.get("offset")
        try:
            result = category_grup.fetch_all(limit, offset)
        except Exception:
            return result.response(500, "Internal Failure")
        else:
            return result.response(200, "category grup data", result)

class CategoryGrupByID(Resource):
    def get(self, id):
        pass