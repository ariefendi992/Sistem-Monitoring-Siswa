from datetime import datetime
from app.extensions import db
from flask import Blueprint, jsonify, request
from app.lib.status_code import *
from app.models.base_model import BaseModel
from app.models.user_model import UserDetailModel, UserModel
from app.models.siswa_model import SiswaModel
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
import datetime

auth = Blueprint('auth', __name__, url_prefix='/auth')

# ------------- user new user details ----------
# ------------- add new user -------
@auth.post('register-new-user')
def insert_new_user():
    # ========== Data Akun ==============
    username = request.json.get('username')
    group = request.json.get('group')
    password = request.json.get('password')
    email = request.json.get('email')

    user = BaseModel(UserModel(username, group, password, email))

    check_username = user.filter_by(username=username)
    check_email = user.filter_by(email=email)

    if check_username is not None:
        return jsonify({
            'error' : f'akun dengan username : {username} sudah ada.'
        }), HTTP_409_CONFLICT
    elif check_email is not None:
         return jsonify({
            'error' : f'akun dengan email : {email} sudah ada.'
        }), HTTP_409_CONFLICT
    else:
       
        # user_group = user.table.group
        if 'admin' in group:
            user.insert_data()
            user_id = user.table.ID
            # ========== Data Profil ==============
            # user_id = request.json.get('user_id')
            nama_depan = request.json.get('nama_depan')
            nama_belakang = request.json.get('nama_belakang')
            jenis_kelamin = request.json.get('jenis_kelamin')
            alamat = request.json.get('alamat')
            telp = request.json.get('telp')

            user_detail = BaseModel(
                                    UserDetailModel(
                                    user_id, 
                                    nama_depan, 
                                    nama_belakang, 
                                    jenis_kelamin, 
                                    alamat, 
                                    telp)
                                )
            user_detail.insert_data()
            return jsonify({
                'ID' : user.table.ID,
                'username' : user.table.username,
                'email' : user.table.email,
                'nama_depan' : user_detail.table.nama_depan,
                'nama_belakang' : user_detail.table.nama_belakang,
                'jenis_kelamin' : user_detail.table.jenis_kelamin,
                'alamat' : user_detail.table.alamat,
                'telp' : user_detail.table.telp
            }), HTTP_201_CREATED
        elif 'siswa' in group:
            user.insert_data()
            user_id = user.table.ID

            nama_siswa = request.json.get('nama_siswa')
            nisn = request.json.get('nisn')
            jk = request.json.get('jenis_kelamin')
            agama = request.json.get('agama')
            alamat = request.json.get('alamat')

            siswa = BaseModel(SiswaModel(user_id, nisn, nama_siswa, jk, agama))
            siswa.insert_data()
            return jsonify({
                'ID' : user.table.ID,
                'username' : user.table.username,
                'email' : user.table.email,
                'nama_siswa' : siswa.table.nama_siswa,
                'nisn' : siswa.table.nisn,
                'jk' : siswa.table.jenis_kelamin,
            }), HTTP_201_CREATED
            

@auth.route('/login', methods=['GET','POST'])
def login_user():
    username = request.json.get('username')
    password = request.json.get('password')
    group = request.json.get('role')

    user = BaseModel(UserModel)
    sql_user = user.filter_by(username=username)

    if not sql_user:
        return jsonify({
            'msg' : 'Username belum terdaftar'
        }), HTTP_401_UNAUTHORIZED

    if sql_user:
        is_pass_correct = UserModel.check_pw_hash(sql_user.password, password)
        
        if not is_pass_correct:
            return jsonify({
                'msg' : 'Password salah!, silahkan periksa kembali'
            }), HTTP_401_UNAUTHORIZED

        elif is_pass_correct:
            generate_token = {
                'id' : sql_user.ID,
                'username' : sql_user.username,
                'group' : sql_user.group
            }

            expire_token = datetime.timedelta(minutes=60)
            expire_refresh_token = datetime.timedelta(days=30)
            
            access = create_access_token(generate_token, fresh=True, expires_delta=expire_token)
            refresh = create_refresh_token(generate_token, expires_delta=expire_refresh_token)

            return jsonify({
                'id' : sql_user.ID,
                'username' : sql_user.username,
                'group' : sql_user.group,
                'token' : access,
                'refresh' : refresh,
                'expire' : str(expire_token)
            }), HTTP_200_OK

    return jsonify({
        'msg' : 'Kesalahan pada autentikasi'
    }), HTTP_401_UNAUTHORIZED