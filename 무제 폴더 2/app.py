from flask import Flask
from flask_smorest import Api
from api import blp as LibraryBlueprint

def create_app():
    app = Flask(__name__)
    app.config.update({
        "API_TITLE": "도서 API",
        "API_VERSION": "1.0",
        "OPENAPI_VERSION": "3.0.3",
        "OPENAPI_URL_PREFIX": "/",
        "OPENAPI_SWAGGER_UI_PATH": "/docs",
        "OPENAPI_SWAGGER_UI_URL": "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    })

    api = Api(app)
    api.register_blueprint(LibraryBlueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)