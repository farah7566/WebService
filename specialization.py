import uuid
from flask import abort, request
from flask_smorest import Blueprint
from flask.views import MethodView
from database import specializations
# add
from schemas import SpecializationSchema

blp = Blueprint("specialization", __name__, description="Operations on specialization")

@blp.route("/specialization/<string:specialization_id>")
class Specialization(MethodView):
    def get(self, specialization_id):
        try:
            # Here you might also want to add the course_items in this specialization
            # We'll do that later on in the course
            return specializations[specialization_id]
        except KeyError:
            abort(404, message="Specialization not found.")

    def delete(self, specialization_id):
        try:
            del specializations[specialization_id]
            return {"message": "Specialization deleted."}
        except KeyError:
            abort(404, message="Specialization not found.")

@blp.route("/specialization")
class SpecializationList(MethodView):
    def get(self):
        return {"specializations": list(specializations.values())}

    @blp.arguments(SpecializationSchema)
    # def post(self):
    def post(self, specialization_data):
        # comment
        # specialization_data = request.get_json()
        # if "name" not in specialization_data:
        #     abort(
        #         400,
        #         message="Bad request. Ensure 'name' is included in the JSON payload.",
        #     )
        # for specialization in specializations.values():
        #     if specialization_data["name"] == specialization["name"]:
        #         abort(400, message=f"Specialization already exists.")
        specialization_id = uuid.uuid4().hex
        specialization = {**specialization_data, "id": specialization_id}
        specializations[specialization_id] = specialization
        return specialization
