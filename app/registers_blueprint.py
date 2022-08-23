from app.controllers.user.user_controller import user
from app.controllers.guru.guru_controller import guru
from app.controllers.auth.auth_controller import auth
from app.controllers.siswa.siswa_controller import siswa
from app.controllers.data_umum.mapel_controller import mapel
from app.controllers.data_umum.kelas_controller import kelas
from app.controllers.data_umum.semester_controller import sms
from app.controllers.data_umum.tahun_ajaran_controller import ta
from app.controllers.data_umum.mengajar_controller import mengajar

def register_app(app):
    app.register_blueprint(user)
    app.register_blueprint(guru)
    app.register_blueprint(auth)
    app.register_blueprint(siswa)
    app.register_blueprint(mapel)
    app.register_blueprint(kelas)
    app.register_blueprint(sms)
    app.register_blueprint(ta)
    app.register_blueprint(mengajar)