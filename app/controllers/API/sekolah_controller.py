from app.models.sekolah_model import *
from flask import Blueprint, request, jsonify
from app.models.base_model import BaseModel
from app.lib.status_code import *

sekolah = Blueprint('sekolah', __name__, url_prefix='/sekolah')

# Mata Pelajaran
# add mapel
@sekolah.post('add-mapel')
def add_mapel():    
    mapel = request.json.get('mapel')
    
    query_mapel = BaseModel(MapelModel(mapel))    
    query_mapel.insert_data()
    
    return jsonify({
        'id' : query_mapel.table.mapel_ID,
        'mapel' : query_mapel.table.mapel
    }), HTTP_201_CREATED

# fetch all mapel
@sekolah.get('/fetch-mapel')
def fetch_mapel():
    query_mapel = BaseModel(MapelModel)
    
    data = []
    for i in query_mapel.fetch_all():
        data.append({
            'id' : i.mapel_ID,
            'mapel' : i.mapel
        })
    print(query_mapel.fetch_all())    
    
    return jsonify({
        'data' : data
    }), HTTP_200_OK
    
# update mapel
@sekolah.put('/update-mapel')
@sekolah.patch('/update-mapel')
def update_mapel():
    mapel = request.json.get('mapel')
    
    ID = request.args.get('id')
    query_mapel = BaseModel(MapelModel)
    mapels = query_mapel.filter_by(mapel_ID=ID)
    
    if not mapels:
        return jsonify({
            'msg' : 'Mapel not found'
        }), HTTP_404_NOT_FOUND
    
    mapels.mapel = mapel
    query_mapel.update_data()
    
    return jsonify({
        'id' : mapels.mapel_ID,
        'mapel' : mapels.mapel
    }), HTTP_200_OK

# delete mapel
@sekolah.route('/delete-mapel/<id>', methods=['DELETE','GET'])
def delete_mapel(id):
    mapel_query = BaseModel(MapelModel)
    sql_mapel = mapel_query.filter_by(mapel_ID=id)
    if not sql_mapel:
        return jsonify({
            'msg' : 'Mapel not found'
        }), HTTP_404_NOT_FOUND
    
    return jsonify({
        'msg' : 'Mapel has been deleted'
    }), HTTP_200_OK
    
# Kelas
# add kelas 
@sekolah.post('/add-kelas')
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
@sekolah.get('/fetch-kelas')
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
@sekolah.put('update-kelas')
@sekolah.patch('update-kelas')
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
@sekolah.delete('/delete-kelas/<id>')
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