from flask import Blueprint, jsonify, request
from app.lib.status_code import HTTP_201_CREATED, HTTP_409_CONFLICT

from app.models.base_model import BaseModel
from app.models.guru_model import GuruModel
from app.models.user_model import UserModel

guru = Blueprint('guru', __name__, url_prefix='/guru')

@guru.route('/add-guru', methods=['POST'])
def tambah_guru():

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
        if 'guru' in group:
            user.insert_data()
            user_id = user.table.ID


            nip = request.json.get('nip')
            nama_guru = request.json.get('nama_guru')
            jenis_kelamin = request.json.get('jenis_kelamin')
            alamat = request.json.get('alamat')
            agama = request.json.get('agama')

            guru = BaseModel(GuruModel(user_id=user_id, nip=nip, nama_guru=nama_guru, jenis_kelamin=jenis_kelamin,
                            alamat=alamat, agama=agama))

            guru.insert_data()
            return jsonify({
                'ID' : user.table.id,
                'username' : user.table.username,
                'email' : user.table.email,
                'group' : user.table.group,
                'nama' : guru.table.nama_guru,
                'jenis_kelamin' : guru.table.jenis_kelamin,
                'agama' : guru.table.agama,
                'alamat' : guru.table.alamat,
            }), HTTP_201_CREATED