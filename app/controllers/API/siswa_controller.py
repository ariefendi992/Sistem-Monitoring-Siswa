from flask import Blueprint
from app.models.siswa_model import SiswaModel

siswa = Blueprint('siswa', __name__, url_prefix='/siswa')

@siswa.post('/add-new-siswa')
def add_new_siswa():
    pass