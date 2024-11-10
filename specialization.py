from flask import abort, request
from flask_smorest import Blueprint
import uuid
from flask.views import MethodView
from database import specializations,course_items

blp=Blueprint("specialization",__name__,description="Operations")


@blp.route("/specialization/<string:specialization_id>")
class Specialization(MethodView):
    def get(self,specialization_id):
        try: 
            return specializations[specialization_id]
        except KeyError:
            #return {"message": "Specialization not found"}, 404
            abort(404, message = "Specialization not found")
    def delete(self,specialization_id):
            try:
                del specializations[specialization_id]
                return{"message":"sprcialization deleted"}
            except KeyError:
                abort(404,message="Specialization not found")


@blp.route("/specialization")

class specialiationlist(MethodView):
    def get(self):
        return {"specializations": list(specializations.values())}
    def post(self):
        specialization_data = request.get_json()
        if "name" not in specialization_data:
            abort(400, message = "BAD REQUEST, Ensure 'name' is included is included in the JSON file")
        for specialization in specializations.values():
            if specialization_data["name"] == specialization["name"]:
                abort(400, message = "Specialization Already Exists")
        
        specialization_id = uuid.uuid4().hex
        specialization = {**specialization_data, "id":specialization_id}
        specializations[specialization_id] = specialization
        #new_specialization = {"name": request_data["name"], "course_items": []}
        #specializations.append(new_specialization)
        return specialization, 201
