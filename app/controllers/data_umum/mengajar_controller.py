# from flask import Blueprint, request, jsonify
from app.lib.status_code import *
from app.models.mengajar_model import MengajarModel
from app.models.base_model import BaseModel
from flask import Blueprint, request, jsonify
import time


mengajar = Blueprint('mengajar', __name__, url_prefix='/mengajar')

@mengajar.route('/add', methods=['GET','POST'])
def add_mengajar():
    kode_mengajar = 'MPL-'+str(time.time()).rsplit('.',1)[1]
    hari = request.json.get('hari')
    jamke = request.json.get('jamke')
    guru_id = request.json.get('guru_id')
    mapel_id = request.json.get('mapel_id')
    kelas_id = request.json.get('kelas_id')
    sms_id = request.json.get('sms_id')
    ta_id = request.json.get('ta_id')
    
    tb = BaseModel(MengajarModel(kode_mengajar, hari, jamke, guru_id, mapel_id, kelas_id, sms_id, ta_id))
    if request.method == 'POST':
        tb.insert_data()
        
        return jsonify({
            'id' : tb.table.mengajar_ID,
            'kd_mengajar' : tb.table.kode_mengajar,
            'hari' : tb.table.hari,
            'jamke' : tb.table.jamke,
            'mapel_id' : tb.table.mapel_id,
        }), HTTP_201_CREATED
    
    else:
        return jsonify({
            'msg' : 'wrong method, please check mengajar conttoller add'
        }), HTTP_405_METHOD_NOT_ALLOWED
        
@mengajar.put('edit/<id>')
@mengajar.patch('edit/<id>')
def edit_mengajar(id):
    hari = request.json.get('hari')
    jamke = request.json.get('jamke')
    guru_id = request.json.get('guru_id')
    mapel_id = request.json.get('mapel_id')
    kelas_id = request.json.get('kelas_id')
    sms_id = request.json.get('sms_id')
    ta_id = request.json.get('ta_id')
    
    tb = BaseModel(MengajarModel)
    id = tb.filter_by(mengajar_ID=id)
    
    id.hari = hari
    id.jamke = jamke
    id.guru_id = guru_id
    id.mapel_id = mapel_id
    id.kelas_id = kelas_id
    id.semester_id = sms_id
    id.th_ajaran_id = ta_id
    
    if request.method == 'PUT' or request.method == 'PATCH':
        tb.update_data()
        
        return jsonify({
            'id' : id.mengajar_ID,
            'kd_mengajar' : id.kode_mengajar,
            'hari' : id.hari,
            'jamke' : id.jamke,
            'mapel_id' : id.mapel_id,
        }), HTTP_200_OK
        
@mengajar.delete('/delete/<id>')
def delete_mengajar(id):
    tb = BaseModel(MengajarModel)
    id = tb.filter_by(mengajar_ID=id)
    
    if request.method == 'DELETE':
        tb.delete_data(id)
        
        return jsonify({
            'msg' : 'Data mengajar has been deleted.'
        }), HTTP_200_OK
        
    else:
        return jsonify({
            'msg' : 'Failed load data'
        }), HTTP_405_METHOD_NOT_ALLOWED