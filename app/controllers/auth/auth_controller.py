from datetime import datetime
from app.extensions import db
from flask import Blueprint, jsonify, request
from app.lib.status_code import *
from app.lib.custome.time_zone import utc_makassar
from app.models.base_model import BaseModel
from ...models.guru_model import GuruModel
from app.models.user_model import UserDetailModel, UserModel
from app.models.siswa_model import SiswaModel
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
import datetime

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.post('/user-login')
def user_login2():
    username = request.json.get('username')
    password = request.json.get('password')

    query = BaseModel(UserModel)
    sql_user = query.filter_by(username=username)

    if not sql_user:
        return jsonify({
            'msg' : 'Username tidak ditemukan.'
        }), HTTP_401_UNAUTHORIZED

    if sql_user:
        check_password = UserModel.check_pw_hash(sql_user.password, password)

        if not check_password:
            return jsonify({
                'msg' : 'Password salah.'
            }), HTTP_401_UNAUTHORIZED
        
        else:
            print(check_password)
            if sql_user.group == 'admin' and sql_user.active == 1:
                query_user_detail = BaseModel(UserDetailModel)
                sql_user_detail = query_user_detail.filter_by(user_id=sql_user.ID)

                sql_user.last_login = utc_makassar()
                query.update_data()

                return jsonify({
                    'id' : sql_user.ID,
                    'username' : sql_user.username,
                    'group' : sql_user.group,
                    'nama_depan' : sql_user_detail.nama_depan,
                    'nama_belakang' : sql_user_detail.nama_belakang,
                    'jenis_kelamin' : sql_user_detail.jenis_kelamin,
                    'alamat' : sql_user_detail.alamat,
                    'telp' : sql_user_detail.telp,
                }), HTTP_200_OK

            elif sql_user.group == 'siswa' and sql_user.active == 1:
                query_siswa = BaseModel(SiswaModel)
                sql_siswa = query_siswa.filter_by(user_id=sql_user.ID)
                
                if not sql_siswa:
                    return jsonify({
                        'msg' : 'Username not full registered'
                    })

                sql_user.last_login = utc_makassar()
                query.update_data()
                
                return jsonify({
                    'id' : sql_user.ID,
                    'username' : sql_user.username,
                    'group' : sql_user.group,
                    'group' : sql_user.group,
                    'nama_depan' : sql_siswa.nama_depan,
                    'nama_belakang' : sql_siswa.nama_belakang,
                    'jenis_kelamin' : sql_siswa.jenis_kelamin,
                    'alamat' : sql_siswa.alamat,
                    'kelas_id' : sql_siswa.kelas_id,
                
                }), HTTP_200_OK
                
            elif sql_user.group == 'guru' and sql_user.active == 1:
                query_guru = BaseModel(GuruModel)
                sql_guru = query_guru.filter_by(user_id=sql_user.ID)
                if not sql_guru:
                    return jsonify({
                        'msg' : 'User not full registered'
                    }), HTTP_404_NOT_FOUND
                if sql_guru.mapel_id is not None:                 
                    sql_user.last_login = utc_makassar()
                    query.update_data()
                    
                    return jsonify({
                        'id' : sql_user.ID,
                        'username' : sql_user.username,
                        'group' : sql_user.group,                        
                        'nama_depan' : sql_guru.nama_depan,
                        'nama_belakang' : sql_guru.nama_belakang,
                        'jenis_kelamin' : sql_guru.jenis_kelamin
                    }), HTTP_200_OK
                else:
                    return jsonify({
                        'msg' : 'Hanya guru Mapel yang dapat mengakses aplikasi ini.'
                        # 'msg' : 'sorry this application can only be accessed by subject teachers'
                    }), HTTP_401_UNAUTHORIZED
            else:
                return jsonify({
                    'msg' : 'Akun sementara tidak dapat di akses. Silahkan kontak admin.'
                }), HTTP_401_UNAUTHORIZED
# ------------- user new user details ----------
# ------------- add new user -------
# @auth.post('/register-new-user')
# def insert_new_user():
#     # ========== Data Akun ==============
#     username = request.json.get('username')
#     group = request.json.get('group')
#     password = request.json.get('password')

#     user = BaseModel(UserModel(username, group, password))

#     check_username = user.filter_by(username=username)

#     if check_username is not None:
#         return jsonify({
#             'error' : f'akun dengan username : {username} sudah ada.'
#         }), HTTP_409_CONFLICT
#    
#     else:
       
#         # user_group = user.table.group
#         if 'admin' in group:
#             user.insert_data()
#             user_id = user.table.ID
#             # ========== Data Profil ==============
#             # user_id = request.json.get('user_id')
#             nama_depan = request.json.get('nama_depan')
#             nama_belakang = request.json.get('nama_belakang')
#             jenis_kelamin = request.json.get('jenis_kelamin')
#             alamat = request.json.get('alamat')
#             telp = request.json.get('telp')

#             user_detail = BaseModel(
#                                     UserDetailModel(
#                                     user_id, 
#                                     nama_depan, 
#                                     nama_belakang, 
#                                     jenis_kelamin, 
#                                     alamat, 
#                                     telp)
#                                 )
#             user_detail.insert_data()
#             return jsonify({
#                 'ID' : user.table.ID,
#                 'username' : user.table.username,
#                 'nama_depan' : user_detail.table.nama_depan,
#                 'nama_belakang' : user_detail.table.nama_belakang,
#                 'jenis_kelamin' : user_detail.table.jenis_kelamin,
#                 'alamat' : user_detail.table.alamat,
#                 'telp' : user_detail.table.telp
#             }), HTTP_201_CREATED
            
#         elif 'siswa' in group:
#             user.insert_data()
#             user_id = user.table.ID

#             nama_depan = request.json.get('nama_depan')
#             nama_belakang = request.json.get('nama_belakang')
#             nisn = request.json.get('nisn')
#             jk = request.json.get('jenis_kelamin')
#             agama = request.json.get('agama')
#             alamat = request.json.get('alamat')

#             siswa = BaseModel(SiswaModel(user_id, nisn, nama_depan, nama_belakang, jk, agama))
#             siswa.insert_data()
#             return jsonify({
#                 'ID' : user.table.ID,
#                 'username' : user.table.username,
#                 'nama_depan' : siswa.table.nama_depan,
#                 'nama_belakang' : siswa.table.nama_belakang,
#                 'nisn' : siswa.table.nisn,
#                 'jk' : siswa.table.jenis_kelamin,
#             }), HTTP_201_CREATED
            
#         elif 'guru':
#             user.insert_data()
#             user_id = user.table.ID
#             nip = request.json.get('nip')
#             nama_depan = request.json.get('nama_depan')
#             nama_belakang = request.json.get('nama_belakang')
#             jenis_kelamin = request.json.get('jenis_kelamin')
#             alamat = request.json.get('alamat')
#             agama = request.json.get('agama')
            
#             query_guru = BaseModel(GuruModel(user_id, nip, nama_depan, nama_belakang, jenis_kelamin,
#                                         alamat, agama))
#             query_guru.insert_data()
            
#             return jsonify({
#                 'ID' : user.table.ID,
#                 'username' : user.table.username,
#                 'nama' : query_guru.table.nama_depan + ' ' +   query_guru.table.nama_belakang,
#                 'nip' : query_guru.table.nip
#             }), HTTP_201_CREATED
        
        
# user login with flask jwt extended
# @auth.route('/login', methods=['GET','POST'])
# def user_login():
#     username = request.json.get('username')
#     password = request.json.get('password')
#     group = request.json.get('role')

#     user = BaseModel(UserModel)
#     sql_user = user.filter_by(username=username)

#     if not sql_user:
#         return jsonify({
#             'msg' : 'Username belum terdaftar'
#         }), HTTP_401_UNAUTHORIZED

#     if sql_user:
#         is_pass_correct = UserModel.check_pw_hash(sql_user.password, password)
        
#         if not is_pass_correct:
#             return jsonify({
#                 'msg' : 'Password salah!, silahkan periksa kembali'
#             }), HTTP_401_UNAUTHORIZED

#         elif is_pass_correct:
#             generate_token = {
#                 'id' : sql_user.ID,
#                 'username' : sql_user.username,
#                 'group' : sql_user.group
#             }

#             expire_token = datetime.timedelta(minutes=60)
#             expire_refresh_token = datetime.timedelta(days=30)
            
#             access = create_access_token(generate_token, fresh=True, expires_delta=expire_token)
#             refresh = create_refresh_token(generate_token, expires_delta=expire_refresh_token)

#             return jsonify({
#                 'id' : sql_user.ID,
#                 'username' : sql_user.username,
#                 'group' : sql_user.group,
#                 'token' : access,
#                 'refresh' : refresh,
#                 'expire' : str(expire_token)
#             }), HTTP_200_OK

#     return jsonify({
#         'msg' : 'Kesalahan pada autentikasi'
#     }), HTTP_401_UNAUTHORIZED

# user login without flask jwt extended
