from flask import Blueprint, jsonify, request
from ...lib.status_code import *
from ...models.user_model import UserModel
from ...models.sekolah_model import KelasModel
from ...models.base_model import BaseModel
from app.models.siswa_model import SiswaModel

siswa = Blueprint('siswa', __name__, url_prefix='/siswa')

@siswa.get('/get-one-siswa/<id>')
def get_one_siswa(id):
    
    query_user = BaseModel(UserModel)
    sql_user = query_user.filter_by(ID=id)
    user_id = sql_user.ID
    
    query_siswa = BaseModel(SiswaModel)
    sql_siswa = query_siswa.filter_by(user_id=user_id)
    
    query_kelas = BaseModel(KelasModel)
    sql_kelas = query_kelas.filter_by(kelas_ID=sql_siswa.kelas_id)
    
    return jsonify({
         'user_id' : sql_user.ID,
        'username' : sql_user.username,
        'group' : sql_user.group,
        'group' : sql_user.group,
        'nama_depan' : sql_siswa.nama_depan,
        'nama_belakang' : sql_siswa.nama_belakang,
        'jenis_kelamin' : sql_siswa.jenis_kelamin,
        'agama' : sql_siswa.agama,
        'alamat' : sql_siswa.alamat,
        'nama_ayah' : sql_siswa.nama_ayah,
        'nama_ibu' : sql_siswa.nama_ibu,
        'foto' : sql_siswa.foto_siswa,
        'kelas' : sql_kelas.nama_kelas
    }), HTTP_200_OK
    
    