from app.controllers.API.user_controller import user
from app.controllers.API.guru_controller import guru

def register_app(app):
    app.register_blueprint(user)
    app.register_blueprint(guru)