from app.lib.status_code import *
from app.models.mapel_model import MapelModel
from app.models.mengajar_model import MengajarModel
from app.models.base_model import BaseModel
from app.models.guru_model import GuruModel
from app.models.kelas_model import KelasModel
from app.models.semester_model import SemesterModel
from app.models.tahun_ajaran_model import TahunAjaranModel
from flask import Blueprint, request, jsonify
from sqlalchemy import and_
from app.extensions import db
import time

from app.models.user_model import UserDetailModel, UserModel


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
        
# join table without foreign Key
@mengajar.get('fetch-data')
def fetch_mengajar():
    # relasi = db.session.query(MengajarModel).add_entity(GuruModel).join(GuruModel, filter).all()
    # relasi = base.join_without_fk((GuruModel, MapelModel) , (MengajarModel.guru_id == GuruModel.guru_ID, MengajarModel.mapel_id == MapelModel.mapel_ID))
    relasi = db.session.query(MengajarModel, GuruModel, MapelModel, KelasModel, SemesterModel, TahunAjaranModel).\
            join(GuruModel, MengajarModel.guru_id == GuruModel.guru_ID). \
            join(MapelModel, MengajarModel.mapel_id == MapelModel.mapel_ID). \
            join(KelasModel, MengajarModel.kelas_id == KelasModel.kelas_ID). \
            join(SemesterModel, MengajarModel.semester_id == SemesterModel.semester_ID ).\
            join(TahunAjaranModel, MengajarModel.th_ajaran_id == TahunAjaranModel.tahun_ajaran_ID)
        
    print(relasi)
    data = []
    for m in relasi:
        print(m)
        data.append({
            'id' : m.MengajarModel.mengajar_ID,
            'kode_mengajar' : m.MengajarModel.kode_mengajar,
            'jamke' : m.MengajarModel.jamke,
            'nama_guru' : m.GuruModel.nama_depan + ' ' + m.GuruModel.nama_belakang,
            'mapel' : m.MapelModel.mapel.upper(),
            'kelas' : m.KelasModel.nama_kelas,
            'semester' : m.SemesterModel.semester.upper() if m.MengajarModel.mengajar_ID == m.SemesterModel.semester_ID else None, 
            't_ajaran' : m.TahunAjaranModel.tahun_ajaran
        })      
        
    return jsonify({
        'data' : data
    }), HTTP_200_OK