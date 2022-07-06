from flask import Flask
from settings import Config
from app.registers_blueprint import register_app

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_app(app)


    return app


def register_extensions(app):
    from app.extensions import db, bcrypt, migrate, jwt

    jwt.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)


app = create_app()