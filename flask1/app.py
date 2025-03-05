from flask import Flask
from library.routes import register_routes

def create_app():
    application = Flask(__name__)
    register_routes(application)
    return application

if __name__ == "__main__":
    app_instance = create_app()
    app_instance.run(debug=True)
