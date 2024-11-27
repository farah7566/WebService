from flask import Flask
from flask_smorest import Api
from courseitems import blp as CourseItemBlueprint
from specialization import blp as SpecializationBlueprint
# Initialize Flask app
app = Flask(__name__)

# Configure API settings
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "TBS REST API"
app.config["API_VERSION"] = "RELEASE 1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


# Initialize Flask-Smorest API
api = Api(app)

# Register Blueprints
api.register_blueprint(CourseItemBlueprint)
api.register_blueprint(SpecializationBlueprint)

if __name__ == '__main__':
    app.run(debug=True)
