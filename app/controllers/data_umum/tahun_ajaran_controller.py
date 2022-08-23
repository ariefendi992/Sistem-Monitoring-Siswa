from flask import Blueprint, request, jsonify
from app.models.tahun_ajaran_model import TahunAjaranModel
from app.models.base_model import BaseModel
from app.lib.status_code import *

ta = Blueprint('tahun_ajaran', __name__, url_prefix='/tahun-ajaran')

@ta.post('/add')
def add_tahun_ajaran():
    ta = request.json.get('ta')
    
    tb  = BaseModel(TahunAjaranModel(ta))
    th_ajaran = tb.filter_by(tahun_ajaran= ta)
    
    if not th_ajaran:
        tb.insert_data()
        return jsonify({
            'id' : tb.table.tahun_ajaran_ID,
            'ta' : tb.table.tahun_ajaran,
            'status' : tb.table.status
        }), HTTP_201_CREATED
        
    else:
        return jsonify({
            'msg' : 'Data is already exist.'
        }), HTTP_409_CONFLICT

@ta.put('/edit/<id>')
@ta.patch('/edit/<id>')
def edit_tahun_ajaran(id):
    ta = request.json.get('ta')
    
    tb  = BaseModel(TahunAjaranModel)
    
    th_ajaran = tb.filter_by(tahun_ajaran_ID=id)
    th_ajaran.tahun_ajaran = ta
    
    if not th_ajaran:
        return jsonify({
            'msg' : 'Data not found'
        }), HTTP_404_NOT_FOUND
    
    else:
        tb.update_data()
        
        return jsonify({
            'id' : th_ajaran.tahun_ajaran_ID,
            'ta' : th_ajaran.tahun_ajaran,
            'status' : th_ajaran.status
        }), HTTP_200_OK
        
@ta.delete('/delete/<id>')
def delete_tahun_ajaran(id):
    tb = BaseModel(TahunAjaranModel)
    id = tb.filter_by(tahun_ajaran_ID=id)
    
    tb.delete_data(id)
    
    return jsonify({
        'msg' : 'Data tahun ajaran has been deleted.'
    }), HTTP_200_OK
    
@ta.get('/fetch')
def fetch_tahun_ajaran():
    tb = BaseModel(TahunAjaranModel)
    
    query_all = tb.fetch_all()
    
    data = []
    for i in query_all:
        data.append({
            'id' : i.tahun_ajaran_ID,
            'ta' : i.tahun_ajaran,
            'status' : i.status
        })
    
    return jsonify({
        'data' : data
    }), HTTP_200_OK
    
        
    