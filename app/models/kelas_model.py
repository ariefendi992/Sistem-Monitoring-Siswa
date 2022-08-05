from app.extensions import db
from sqlalchemy import ForeignKey

class KelasModel(db.Model):
    __tablename__ = 'tb_kelas'
    kelas_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_kelas = db.Column(db.String(128), nullable=False)
    jml_siswa = db.Column(db.String(16), nullable=True)
    guru_id = db.Column(db.Integer, ForeignKey('tb_guru_detail.guru_ID'), nullable=True)
    

    