import datetime
from fileinput import filename
import hashlib
import http
from operator import and_
from flask import Blueprint, jsonify, url_for
from app.lib.custome.time_zone import todayAt
from app.lib.status_code import *
from ...models.user_model import UserModel
from ...models.kelas_model import KelasModel
from ...models.base_model import BaseModel
from app.models.siswa_model import SiswaModel
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import HorizontalBarsDrawer
from werkzeug.utils import secure_filename
from app.models.mengajar_model import MengajarModel
from app.models.guru_model import GuruModel
from app.models.kelas_model import KelasModel
from app.models.mapel_model import MapelModel
from app.extensions import db
from sqlalchemy import and_
from app.lib.custome.week_days import *
import qrcode, os

siswa = Blueprint('siswa', __name__, url_prefix='/siswa')

QR_CODE_FOLDER = os.getcwd() + '/app/static/images/siswa'

@siswa.route('/get-one-siswa/<id>', methods=['GET','PUT','POST'])
def get_one_siswa(id):    
    query_user = BaseModel(UserModel)
    sql_user = query_user.filter_by(ID=id)
    
    if not sql_user:
        return jsonify({
            'msg' : 'User not found'
        }), HTTP_404_NOT_FOUND
    
    user_id = sql_user.ID
    query_siswa = BaseModel(SiswaModel)
    sql_siswa = query_siswa.filter_by(user_id=user_id)
    
    query_kelas = BaseModel(KelasModel)
    sql_kelas = query_kelas.filter_by(kelas_ID=sql_siswa.kelas_id)
    
    qr_code = url_for('static', filename='images/siswa/qr code/'+ sql_siswa.qr_code) if sql_siswa.qr_code else None
    
    file = os.path.exists(f'app/static/images/siswa/qr code/{sql_siswa.qr_code}')
    
    print('File ada ==', file)    
    
    if file == False:
        sql_siswa.qr_code = None
        query_siswa.update_data()
    
    return jsonify({
        'user_id' : sql_user.ID,
        'username' : sql_user.username,
        'group' : sql_user.group,
        'group' : sql_user.group,
        'nisn' : sql_siswa.nisn,
        'nama_depan' : sql_siswa.nama_depan,
        'nama_belakang' : sql_siswa.nama_belakang,
        'jenis_kelamin' : sql_siswa.jenis_kelamin,
        'agama' : sql_siswa.agama,
        'alamat' : sql_siswa.alamat,
        'foto' : sql_siswa.foto_siswa,
        'kelas' : sql_kelas.nama_kelas if sql_siswa.kelas_id else None,
        'qr_code' : qr_code if file == True else None,
    }), HTTP_200_OK
    
@siswa.route('/generate-qrcode/<id>', methods=['POST','PUT','PATCH'])
def generate_qrcode(id):
    query_user = BaseModel(UserModel)
    sql_user = query_user.filter_by(ID=id)
    user_id = sql_user.ID
    
    query_siswa = BaseModel(SiswaModel)
    sql_siswa = query_siswa.filter_by(user_id=user_id)
    
    qr= qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(sql_siswa.nisn)
    qr_img = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer())
    
    enc_file_name = hashlib.md5(secure_filename(sql_user.username).encode('utf-8')).hexdigest()
    path_file = QR_CODE_FOLDER + '/qr code/'+  sql_siswa.nama_depan + '_' + enc_file_name + '.png'
    qr_img.save(path_file)
    
    sql_siswa.qr_code = sql_siswa.nama_depan + '_' + enc_file_name + '.png'
    
    query_siswa.update_data()
    
    qr_code = url_for('static', filename='images/siswa/qr code/'+ sql_siswa.qr_code) if sql_siswa.qr_code else None    
    return jsonify({
        'id' : sql_user.ID,
        'nama_depan' : sql_siswa.nama_depan,
        'nama_belakang' : sql_siswa.nama_belakang,
        'qr_code' : qr_code 
    }), HTTP_200_OK
    
@siswa.get('/jadwal/<kelas_id>')
def jadwal_belajar(kelas_id):
    
    table = BaseModel(MengajarModel)
    kelas_id = table.filter_by(kelas_id=kelas_id)
    
    if kelas_id:        
        # today_sql = table.fetch_all()
        today = []
        
        today_sql = db.session.query(MengajarModel, GuruModel, MapelModel, KelasModel)\
            .join(GuruModel, MengajarModel.guru_id == GuruModel.guru_ID)\
            .join(MapelModel, MengajarModel.mapel_id == MapelModel.mapel_ID)\
            .join(KelasModel, MengajarModel.kelas_id == KelasModel.kelas_ID)\
            .filter(MengajarModel.hari == today_()).all()
                
        print('today =',today_sql)        
        
        for m in today_sql:
                today.append({
                'id' : m.MengajarModel.mengajar_ID,
                'nama_guru' : m.GuruModel.nama_depan.capitalize() + ' ' + m.GuruModel.nama_belakang.capitalize(),
                'hari' : m.MengajarModel.hari.capitalize(),
                'kelas' : m.KelasModel.nama_kelas,
                'jam_mulai' : m.MengajarModel.mulai,
                'jam_selesai' : m.MengajarModel.selesai,
                'mapel' : m.MapelModel.mapel.upper()
            })
            
    
        tomorrow_sql = db.session.query(MengajarModel, GuruModel, MapelModel, KelasModel)\
            .join(GuruModel, MengajarModel.guru_id == GuruModel.guru_ID)\
            .join(MapelModel, MengajarModel.mapel_id == MapelModel.mapel_ID)\
            .join(KelasModel, MengajarModel.kelas_id == KelasModel.kelas_ID)\
            .filter(MengajarModel.hari == tomorrow_()).all()
                
        tomorrow = []      
        
        for m in tomorrow_sql:
                tomorrow.append({
                'id' : m.MengajarModel.mengajar_ID,
                'nama_guru' : m.GuruModel.nama_depan.capitalize() + ' ' + m.GuruModel.nama_belakang.capitalize(),
                'hari' : m.MengajarModel.hari.capitalize(),
                'kelas' : m.KelasModel.nama_kelas,                
                'jam_mulai' : m.MengajarModel.mulai,
                'jam_selesai' : m.MengajarModel.selesai,
                'mapel' : m.MapelModel.mapel.upper()
            })
            
        return jsonify({
            'data' : {
                'today' : today if today else 'Hari Libur',
                'tomorrow' : tomorrow if tomorrow else 'Hari Libur'
            }
        }), HTTP_200_OK
        
    else:
        return jsonify({
            'msg' : 'Belum ada jadwal.'
        })

@siswa.get('/one-mapel/<kelas_id>')
def get_one_mapel(kelas_id):
    table = BaseModel(MengajarModel)
    
    sql_jadwal = table.filter_by(kelas_id=kelas_id)
    
    if sql_jadwal:        
        now = datetime.datetime.now()
        hours_to_str =datetime.datetime.strftime(now, "%H:%M")
        day = day_now_indo()
        day_indo = day[0] +', '+str(day[1]) + ' ' + day[2] + ' ' + str(day[3])
        
        sql_jadwal_now = db.session.query(MengajarModel, MapelModel, GuruModel).\
            join(MapelModel, MengajarModel.mapel_id == MapelModel.mapel_ID).\
            join(GuruModel, MengajarModel.guru_id == GuruModel.guru_ID).\
                filter(and_(MengajarModel.mulai <=hours_to_str,
                            MengajarModel.selesai >=hours_to_str, 
                            MengajarModel.hari == day[0].lower())).first()
        
        print(sql_jadwal_now)
        if sql_jadwal_now is not None:
            
            print(sql_jadwal_now.MapelModel.mapel)
        
            data = []
            data.append({
                'id' : sql_jadwal_now.MengajarModel.mengajar_ID,
                'mapel' : sql_jadwal_now.MapelModel.mapel.upper(),
                'guru' : sql_jadwal_now.GuruModel.nama_depan.capitalize() + ' ' +  sql_jadwal_now.GuruModel.nama_belakang.capitalize(),
                'mulai' : sql_jadwal_now.MengajarModel.mulai,
                'selesai' : sql_jadwal_now.MengajarModel.selesai,
                'date' : day_indo
            })
            
            return jsonify({
                # 'data' : data
                'id' : sql_jadwal_now.MengajarModel.mengajar_ID,
                'mapel' : sql_jadwal_now.MapelModel.mapel.upper(),
                'nama_guru' : sql_jadwal_now.GuruModel.nama_depan.capitalize() + ' ' +  sql_jadwal_now.GuruModel.nama_belakang.capitalize(),
                'jam_mulai' : sql_jadwal_now.MengajarModel.mulai,
                'jam_selesai' : sql_jadwal_now.MengajarModel.selesai,
                'hari' : day_indo
                }), HTTP_200_OK
        else:
            day = day_now_indo()
            return jsonify({
                'data' : day[0] +', '+str(day[1]) + ' ' + day[2] + ' ' + str(day[3])
            }),HTTP_404_NOT_FOUND
        
    else:
        return jsonify({
            'error' : 'Data not found'
        }), HTTP_404_NOT_FOUND
    
    # if sql_jadwal_now.mulai is not None:
    #     convert_str_to_hours = datetime.datetime.strptime(sql_jadwal_now.mulai, '%H:%M')
    #     hours_now = datetime.datetime.now()
    #     if hours_now >= todayAt(convert_str_to_hours.hour, convert_str_to_hours.minute):
    #         return jsonify({
    #             'id' : sql_jadwal_now.mengajar_ID
    #         }), HTTP_200_OK
    
    # else:
    #     return jsonify({
    #         'msg' : 'Jam Mulai masih kosong'
    #     }), HTTP_404_NOT_FOUND
            
   