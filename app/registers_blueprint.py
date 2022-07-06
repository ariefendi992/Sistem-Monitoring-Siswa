from app.controllers.API.user_controller import user

def register_app(app):
    app.register_blueprint(user)