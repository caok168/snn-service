__version__ = '0.0.19'

from .app import Flask
from flask_docs import ApiDoc
from flask_cors import *
from app.api.v1 import create_blueprint_v1
import os


def register_blueprints(app):

    app.register_blueprint(create_blueprint_v1(), url_prefix='/api')


def create_app():
    app = Flask(__name__, static_folder='../static', static_url_path='', template_folder='../static')

    CORS(app, resources={r"/*": {"origins": "*"}}, send_wildcard=True)

    # database_url = os.environ.get('OC_DB_URL', "postgresql://admin:admin123456@127.0.0.1:5432/manager")
    # print("database_url:{}".format(database_url))

    # app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    # app.config["SECRET_KEY"] = '1c0049e9387f42f2a5da2ec692f3c6d0'
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config["API_DOC_MEMBER"] = ['api/cases', 'api/images', 'api/tasks']

    app_settings = os.getenv('APP_SETTINGS', 'app.config.DevelopmentConfig')
    app.config.from_object(app_settings)

    ApiDoc(app)

    register_blueprints(app)

    return app
