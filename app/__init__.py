from flask import Flask

from app.routes.nombres import bp_nombres


from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(bp_nombres)

    return app
