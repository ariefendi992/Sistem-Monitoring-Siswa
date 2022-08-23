from flask import Blueprint, request, jsonify
from app.models.base_model import BaseModel
from app.models.semester_model import SemesterModel
from app.lib.status_code import *

sms = Blueprint('semester', __name__, url_prefix='/sms')

@sms.post('/add')
def add_semester():
    sms = request.json.get('sms')
    
    table = BaseModel(SemesterModel(sms))
    semester = table.filter_by(semester=sms)
    
    if not semester:
        table.insert_data()
        
        return jsonify({
            'id' : table.table.semester_ID,
            'sms' : table.table.semester,
            'status' : table.table.status
        }), HTTP_201_CREATED
        
    else:
        return jsonify({
            'msg' : 'Data semester is already exist.'
        }), HTTP_409_CONFLICT

@sms.put('/edit/<id>')
@sms.patch('/edit/<id>')
def edit_semester(id):
    sms = request.json.get('sms')
    
    tb = BaseModel(SemesterModel)
    
    semester = tb.filter_by(semester_ID=id)

    semester.semester = sms
    
    tb.update_data()
    
    return jsonify({
            'id' : semester.semester_ID,
            'sms' : semester.semester,
            'status' : semester.status
        }), HTTP_200_OK
    
@sms.delete('/delete/<id>')
def delete_semester(id):
    tb = BaseModel(SemesterModel)
    
    id = tb.filter_by(semester_ID=id)
    
    tb.delete_data(id)
    
    return jsonify({
        'msg' : 'Data semester has been deleted.'
    }), HTTP_200_OK

@sms.get('/fetch')
def fetch_semester():
    
    tb = BaseModel(SemesterModel)
    
    query_all = tb.fetch_all()
    
    data = []
    for i in query_all:
        data.append({
            'id' : i.semester_ID,
            'sms' : i.semester,
            'status' : i.status
        })
    
    return jsonify({
      'data' : data
    }), HTTP_200_OK