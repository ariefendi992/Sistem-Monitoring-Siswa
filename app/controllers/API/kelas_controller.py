from flask import Blueprint, request, jsonify
from app.models.base_model import BaseModel
from app.models.kelas_model import KelasModel
from app.lib.status_code import *

kelas = Blueprint('kelas', __name__, url_prefix='/kelas')
# Kelas
# add kelas 
@kelas.post('/add-kelas')
def add_kelas():
    nama_kelas = request.json.get('kelas')
    jml_siswa = request.json.get('jml_siswa')
    
    sql_kelas = BaseModel(KelasModel(nama_kelas, jml_siswa))
    kelas = sql_kelas.filter_by(nama_kelas=nama_kelas)
    if kelas:
        return jsonify({
            'msg' : 'Dat Kelas is already exists.'
        }), HTTP_409_CONFLICT
        
    else:
        sql_kelas.insert_data()
        return jsonify({
            'id': sql_kelas.table.kelas_ID,
            'kelas' : sql_kelas.table.nama_kelas
        }), HTTP_201_CREATED

# fetch kelas
@kelas.get('/fetch-kelas')
def fetch_kelas():
    query = BaseModel(KelasModel)
    sql_kelas = query.fetch_all()
    
    data = []
    for i in sql_kelas:
        data.append({
            'id' : i.kelas_ID,
            'kelas' : i.nama_kelas,
            'jml_siswa' : i.jml_siswa
        })
        
    return jsonify({
        'data' : data
    }), HTTP_200_OK
    
# update kelas
@kelas.put('update-kelas')
@kelas.patch('update-kelas')
def update_kelas():
    nama_kelas = request.json.get('kelas')
    jml_siswa = request.json.get('jml_siswa')
    
    id = request.args.get('id')
    query = BaseModel(KelasModel)
    kelas = query.filter_by(kelas_ID=id)
    
    if not kelas:
        return jsonify({
            'msg' : 'Data Kelas not found'
        }), HTTP_404_NOT_FOUND
    
    kelas.nama_kelas = nama_kelas
    kelas.jml_siswa = jml_siswa
    
    query.update_data()
    
    return jsonify({
        'id' : kelas.kelas_ID,
        'kelas' : kelas.nama_kelas,
        'jml_siswa' : kelas.jml_siswa
    }), HTTP_200_OK
    
# delete kelas
@kelas.delete('/delete-kelas/<id>')
def delete_kelas(id):
    query = BaseModel(KelasModel)
    
    sql_kelas = query.filter_by(kelas_ID=id)
    
    if not sql_kelas:
        return jsonify({
            'msg' : 'Data Kelas not found'
        }), HTTP_404_NOT_FOUND
        
    query.delete_data(sql_kelas)
    
    return jsonify({
        'msg' : 'Data Kelas has been deleted'
    }), HTTP_200_OK