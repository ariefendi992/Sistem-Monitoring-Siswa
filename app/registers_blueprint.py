from app.controllers.API.user_controller import user
from app.controllers.API.guru_controller import guru
from app.controllers.API.auth_controller import auth
from app.controllers.API.siswa_controller import siswa
from app.controllers.API.sekolah_controller import sekolah

def register_app(app):
    app.register_blueprint(user)
    app.register_blueprint(guru)
    app.register_blueprint(auth)
    app.register_blueprint(siswa)
    app.register_blueprint(sekolah)