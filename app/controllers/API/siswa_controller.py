from fileinput import filename
import hashlib
from re import A
from flask import Blueprint, jsonify, url_for
from ...lib.status_code import *
from ...models.user_model import UserModel
from ...models.sekolah_model import KelasModel
from ...models.base_model import BaseModel
from app.models.siswa_model import SiswaModel
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import HorizontalBarsDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from werkzeug.utils import secure_filename
import qrcode, os

siswa = Blueprint('siswa', __name__, url_prefix='/siswa')

QR_CODE_FOLDER = os.getcwd() + '/app/static/images/siswa'

@siswa.route('/get-one-siswa/<id>', methods=['GET','PUT','POST'])
def get_one_siswa(id):    
    query_user = BaseModel(UserModel)
    sql_user = query_user.filter_by(ID=id)
    
    if not sql_user:
        return jsonify({
            'msg' : 'User not found'
        }), HTTP_404_NOT_FOUND
    
    user_id = sql_user.ID
    query_siswa = BaseModel(SiswaModel)
    sql_siswa = query_siswa.filter_by(user_id=user_id)
    
    query_kelas = BaseModel(KelasModel)
    sql_kelas = query_kelas.filter_by(kelas_ID=sql_siswa.kelas_id)
    
    qr_code = url_for('static', filename='images/siswa/qr code/'+ sql_siswa.qr_code) if sql_siswa.qr_code else None
    
    file = os.path.exists(f'app/static/images/siswa/qr code/{sql_siswa.qr_code}')
    
    print('File ada ==', file)    
    
    if file == False:
        sql_siswa.qr_code = None
        query_siswa.update_data()
    
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
        'kelas' : sql_kelas.nama_kelas if sql_siswa.kelas_id else None,
        'qr_code' : qr_code if file == True else None,
    }), HTTP_200_OK
    
@siswa.route('/generate-qrcode/<id>', methods=['POST','PUT','PATCH'])
def generate_qrcode(id):
    query_user = BaseModel(UserModel)
    sql_user = query_user.filter_by(ID=id)
    user_id = sql_user.ID
    
    query_siswa = BaseModel(SiswaModel)
    sql_siswa = query_siswa.filter_by(user_id=user_id)
    
    qr= qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(sql_siswa.nisn)
    qr_img = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer())
    
    enc_file_name = hashlib.md5(secure_filename(sql_user.username).encode('utf-8')).hexdigest()
    path_file = QR_CODE_FOLDER + '/qr code/'+  sql_siswa.nama_depan + '_' + enc_file_name + '.png'
    qr_img.save(path_file)
    
    sql_siswa.qr_code = sql_siswa.nama_depan + '_' + enc_file_name + '.png'
    
    query_siswa.update_data()
    
    qr_code = url_for('static', filename='images/siswa/qr code/'+ sql_siswa.qr_code) if sql_siswa.qr_code else None    
    return jsonify({
        'id' : sql_user.ID,
        'nama_depan' : sql_siswa.nama_depan,
        'nama_belakang' : sql_siswa.nama_belakang,
        'qr_code' : qr_code 
    }), HTTP_200_OK
    

    
    