from flask import Blueprint, jsonify, request
from app.models.guru_model import GuruModel
from app.models.kelas_model import KelasModel
from app.models.siswa_model import SiswaModel
from app.models.user_model import UserModel, UserDetailModel
from app.models.base_model import BaseModel
from app.lib.status_code import *
from app.extensions import db
from sqlalchemy import func

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/register-user', methods=['POST','PUT','PATCH'])
def register_user():

    # ========== Data Akun ==============
    username = request.json.get('username')
    group = request.json.get('group')
    password = request.json.get('password')

    user = BaseModel(UserModel(username, group, password))

    check_username = user.filter_by(username=username)

    if check_username is not None:
        return jsonify({
            'error' : f'akun dengan username : {username} sudah ada.'
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
                'nama_depan' : user_detail.table.nama_depan,
                'nama_belakang' : user_detail.table.nama_belakang,
                'jenis_kelamin' : user_detail.table.jenis_kelamin,
                'alamat' : user_detail.table.alamat,
                'telp' : user_detail.table.telp
            }), HTTP_201_CREATED
            
        elif 'siswa' in group:
            user.insert_data()
            user.insert_data()
            user_id = user.table.ID

            nama_depan = request.json.get('nama_depan')
            nama_belakang = request.json.get('nama_belakang')
            nisn = user.table.username
            jk = request.json.get('jenis_kelamin')
            agama = request.json.get('agama')
            alamat = request.json.get('alamat')
            kelas_id = request.json.get('kelas_id')
            

            siswa = BaseModel(SiswaModel(user_id, nama_depan, nama_belakang, nisn, jk, agama, alamat, kelas_id))
            kelas = BaseModel(KelasModel)
            sql_kelas = kelas.filter_by(kelas_ID=kelas_id)
            print(sql_kelas)
            siswa.insert_data()            
            
            siswa_count_gender = db.session.query(func.count(SiswaModel.kelas_id)).filter(SiswaModel.kelas_id==kelas_id).filter(SiswaModel.jenis_kelamin==jk).scalar()
            siswa_count_all = db.session.query(func.count(SiswaModel.kelas_id)).filter(SiswaModel.kelas_id==kelas_id).scalar()
            if siswa.table.jenis_kelamin == 'laki-laki':
                sql_kelas.jml_laki = siswa_count_gender
                # sql_kelas.jml_siswa = str(siswa_total)            
                # kelas.update_data()
            elif siswa.table.jenis_kelamin == 'perempuan':
                sql_kelas.jml_perempuan = siswa_count_gender
                # sql_kelas.jml_siswa = str(siswa_total)            
                # kelas.update_data()
            sql_kelas.jml_siswa = siswa_count_all            
            kelas.update_data()

                
            
            return jsonify({
                'ID' : user.table.ID,
                'username' : user.table.username,
                'nama_depan' : siswa.table.nama_depan,
                'nama_belakang' : siswa.table.nama_belakang,
                'nisn' : siswa.table.nisn,
            }), HTTP_201_CREATED
            
        elif 'guru':
            user.insert_data()
            user_id = user.table.ID
            nip = user.table.username
            nama_depan = request.json.get('nama_depan')
            nama_belakang = request.json.get('nama_belakang')
            jenis_kelamin = request.json.get('jenis_kelamin')
            alamat = request.json.get('alamat')
            agama = request.json.get('agama')
            
            query_guru = BaseModel(GuruModel(user_id, nip, nama_depan, nama_belakang, jenis_kelamin,
                                        alamat, agama))
            query_guru.insert_data()
            
            return jsonify({
                'ID' : user.table.ID,
                'username' : user.table.username,
                'nama' : query_guru.table.nama_depan + ' ' +   query_guru.table.nama_belakang,
                'nip' : query_guru.table.nip
            }), HTTP_201_CREATED  


# 
# ------------- check password user -----------------
@user.post('/check-password')
def check_password():
    password = request.json.get('password')

    users = BaseModel(UserModel)
    ID = request.args.get('id')
    check_user = users.filter_by(ID=ID)
    if check_user:
        is_pass_correct = UserModel.check_pw_hash(check_user.password, password)
        if is_pass_correct:
            return jsonify({
                'msg' : 'password sesuai.'
            }), HTTP_200_OK

        else:
            return jsonify({
                'msg' : 'password salah.!'
            })

# 
#  ---------------- update password ------------------
@user.route('/update-password', methods=['PUT','PATCH'])
def update_password():
    if request.method == 'PUT' or request.method == 'PATCH':
        password = request.json.get('password')
        
        users = BaseModel(UserModel)
        ID = request.args.get('id')
        check_user = users.filter_by(ID=ID)

        check_user.password = password

        users.update_data()

        return jsonify({
            'msg' : 'update password success.'
        }), HTTP_200_OK

@user.delete('/delete-user')
def delete_user():
    users = BaseModel(UserModel)
    
    ID = request.args.get('id')
    check_user = users.filter_by(ID=ID)
    
    if not check_user:
        return jsonify({
            'msg' : 'User not found'
        }), HTTP_404_NOT_FOUND
        
    users.delete_data(check_user)
    
    return jsonify({
        'msg' : 'User has been deleted'
    }), HTTP_200_OK


# =============== edit user ===========
@user.route('/update-user-detail', methods=['PUT','PATCH','POST'])
def update_detail_user():
    username = request.json.get('username')
    group = request.json.get('group')
    nama_depan = request.json.get('nama_depan')
    nama_belakang = request.json.get('nama_belakang')
    jenis_kelamin = request.json.get('jenis_kelamin')
    alamat = request.json.get('alamat')
    telp = request.json.get('telp')

    users = BaseModel(UserModel)
    ID = request.args.get('id')
    user = users.filter_by(ID=ID)
    
    user.username = username
    user.group = group

    users.update_data()

    user_details = BaseModel(UserDetailModel)
    user_detail = user_details.filter_by(user_id=user.ID)

    # Jika user detail tidak ada
    # maka tambahkan data user detail
    if user_detail is None:
        add_user_detail = BaseModel(UserDetailModel(user.ID, nama_depan,
                                                    nama_belakang, jenis_kelamin,
                                                    alamat, telp))
        add_user_detail.insert_data()
    else:
        user_detail.nama_depan = nama_depan
        user_detail.nama_belakang = nama_belakang
        user_detail.jenis_kelamin = jenis_kelamin
        user_detail.alamat = alamat
        user_detail.telp = telp

        user_details.update_data()

    return jsonify({
        'username' : user.username,
        'group' : user.group,
        'nama_lengkap' : user_detail.nama_depan + ' ' + user_detail.nama_belakang,
    }), HTTP_201_CREATED

    
# fetch all User Detail
@user.route('all-users-detail', methods=['GET'])
def fetch_all_user_detail():
    # query = db.session.query(UserModel).all()
    users = BaseModel(UserModel)
    query = users.fetch_join_all(UserDetailModel)

    print(query)
    list = []
    for u1, u2 in query:
        list.append({
            'username' : u1.username,
            'group' : u1.group,
            'nama_depan' : u2.nama_depan if u2.nama_depan else None,
            'nama_depan' : u2.nama_depan,
            'nama_belakang' : u2.nama_belakang,
            'jenis_kelamin' : u2.jenis_kelamin,
            'alamat' : u2.alamat,
            'telp' : u2.telp,
            'profil_picture' : u2.profil_picture,
        })

    return jsonify({
        'data:' : list
    }), HTTP_200_OK
    
# fetch all user
@user.route('all-users', methods=['GET'])
def fetch_all_user():
    users = BaseModel(UserModel)
    query = users.fetch_all()

    list = []
    for u in query:
        list.append({
            'id' : u.ID,
            'username' : u.username,
            'group' : u.group,
            'last_login' : u.last_login,
            'status_aktif' : 'aktif' if u.active == 1 else 'tidak aktif'
        })

    return jsonify({
        'all_user' : list
    }), HTTP_200_OK
