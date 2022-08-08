from app.controllers.API.user_controller import user
from app.controllers.API.guru_controller import guru
from app.controllers.API.auth_controller import auth

def register_app(app):
    app.register_blueprint(user)
    app.register_blueprint(guru)
    app.register_blueprint(auth)