import email
from flask import Blueprint, jsonify, request
from sqlalchemy import table
from app.models.user_model import UserModel, UserDetailModel
from app.models.base_model import BaseModel
from app.lib.status_code import *

user = Blueprint('user', __name__, url_prefix='/user')
# 
# ------------- register user -----------------
@user.route('/register-user', methods=['POST'])
def register_user():
    username = request.json.get('username')
    group = request.json.get('group')
    password = request.json.get('password')
    email = request.json.get('email')

    users = BaseModel(UserModel(username,group, password, email))

    check_user = users.filter_by(username=username)
    check_email = users.filter_by(email=email)

    if check_user is not None:
        return jsonify({
            'error' : f'akun dengan username : {username} sudah ada.'
        }), HTTP_409_CONFLICT
    elif check_email is not None:
         return jsonify({
            'error' : f'akun dengan email : {email} sudah ada.'
        }), HTTP_409_CONFLICT
    else:
        users.insert_data()
        return jsonify({
            'id' : users.table.ID,
            'username' : users.table.username,
            'email' : users.table.email
        }),HTTP_201_CREATED

# # 
# # ------------- update user -----------------
# @user.route('/update-user', methods=['PUT','PATCH'])
# def update_user():
#     if request.method == 'PUT' or request.method == 'PATCH':
#         username = request.json.get('username')
#         group = request.json.get('group')
#         email = request.json.get('email')

#         users = BaseModel(UserModel)
#         ID = request.args.get('id')
#         check_user = users.filter_by(ID=ID)
#         print(check_user)

#         check_user.username = username
#         check_user.group = group
#         check_user.email = email
#         users.update_data()
#         return jsonify({
#             'id' : check_user.ID,
#             'username' : check_user.username,
#             'email' : check_user.email
#         }), HTTP_201_CREATED

#     else:
#         return jsonify({
#             'error' : 'Not Method Allowed'
#         }), HTTP_405_METHOD_NOT_ALLOWED


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
    users.delete_data(check_user)
    return jsonify({
        'msg' : 'delete data success.'
    }), HTTP_200_OK

# 
# ------------- user new user details ----------
# ------------- add new user -------
@user.post('add-new-user')
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
        user.insert_data()
        user_id = user.table.ID
        if user_id is not None:
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
    
# =============== edit new user ===========
@user.route('/update-user')
def update_detail_user():
    username = request.json.get('username')
    group = request.json.get('group')
    password = request.json.get('password')
    email = request.json.get('email')
    nama_depan = request.json.get('nama_depan')
    nama_belakang = request.json.get('nama_belakang')
    jenis_kelamin = request.json.get('jenis_kelamin')
    alamat = request.json.get('alamat')
    telp = request.json.get('telp')

    