# main.py
import uuid
from flask import Flask, request, abort, jsonify
from database import specializations, course_items

app = Flask(__name__)


@app.get("/course_item/<string:course_item_id>")
def get_course_item(course_item_id):
    try:
        return jsonify(course_items[course_item_id])
    except KeyError:
        abort(404, description="Course item not found.")


@app.post("/course_item")
def create_course_item():
    course_item_data = request.get_json()
    if "type" not in course_item_data or "specialization_id" not in course_item_data or "name" not in course_item_data:
        abort(400,
              description="Bad request. Ensure 'type', 'specialization_id', and 'name' are included in the JSON payload.")

    for course_item in course_items.values():
        if course_item_data["name"] == course_item["name"] and course_item_data["specialization_id"] == course_item[
            "specialization_id"]:
            abort(400, description="Course item already exists.")

    course_item_id = uuid.uuid4().hex
    course_item = {**course_item_data, "id": course_item_id}
    course_items[course_item_id] = course_item
    return jsonify(course_item)


@app.delete("/course_item/<string:course_item_id>")
def delete_course_item(course_item_id):
    try:
        del course_items[course_item_id]
        return jsonify({"message": "Course item deleted."})
    except KeyError:
        abort(404, description="Course item not found.")


@app.put("/course_item/<string:course_item_id>")
def update_course_item(course_item_id):
    course_item_data = request.get_json()
    if "type" not in course_item_data or "name" not in course_item_data:
        abort(400, description="Bad request. Ensure 'type' and 'name' are included in the JSON payload.")

    try:
        course_item = course_items[course_item_id]
        course_item.update(course_item_data)
        return jsonify(course_item)
    except KeyError:
        abort(404, description="Course item not found.")


@app.get("/course_item")
def get_all_course_items():
    return jsonify({"course_items": list(course_items.values())})


@app.get("/specialization/<string:specialization_id>")
def get_specialization(specialization_id):
    try:
        return jsonify(specializations[specialization_id])
    except KeyError:
        abort(404, description="Specialization not found.")


@app.post("/specialization")
def create_specialization():
    specialization_data = request.get_json()
    if "name" not in specialization_data:
        abort(400, description="Bad request. Ensure 'name' is included in the JSON payload.")

    for specialization in specializations.values():
        if specialization_data["name"] == specialization["name"]:
            abort(400, description="Specialization already exists.")

    specialization_id = uuid.uuid4().hex
    specialization = {**specialization_data, "id": specialization_id}
    specializations[specialization_id] = specialization
    return jsonify(specialization)


@app.delete("/specialization/<string:specialization_id>")
def delete_specialization(specialization_id):
    try:
        del specializations[specialization_id]
        return jsonify({"message": "Specialization deleted."})
    except KeyError:
        abort(404, description="Specialization not found.")


@app.get("/specialization")
def get_specializations():
    return jsonify({"specializations": list(specializations.values())})


# Run the application if this file is executed
if __name__ == "__main__":
    app.run(debug=True)

