from app.models.mapel_model import *
from flask import Blueprint, request, jsonify
from app.models.base_model import BaseModel
from app.lib.status_code import *

mapel = Blueprint('mapel', __name__, url_prefix='/mapel')

# Mata Pelajaran
# add mapel
@mapel.post('add-mapel')
def add_mapel():    
    mapel = request.json.get('mapel')
    
    query_mapel = BaseModel(MapelModel(mapel))    
    query_mapel.insert_data()
    
    return jsonify({
        'id' : query_mapel.table.mapel_ID,
        'mapel' : query_mapel.table.mapel
    }), HTTP_201_CREATED

# fetch all mapel
@mapel.get('/fetch-mapel')
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
@mapel.put('/update-mapel')
@mapel.patch('/update-mapel')
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
@mapel.route('/delete-mapel/<id>', methods=['DELETE','GET'])
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
    
