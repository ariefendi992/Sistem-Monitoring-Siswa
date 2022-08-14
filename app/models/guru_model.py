from app.extensions import db   
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import ForeignKey

class GuruModel(db.Model):
    __tablename__ = 'tb_guru_detail'
    guru_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(INTEGER(unsigned=True), ForeignKey('tb_user.ID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    nip = db.Column(db.String(32), nullable=False)
    nama_depan = db.Column(db.String(128), nullable=False)
    nama_belakang = db.Column(db.String(128), nullable=False)
    jenis_kelamin = db.Column(db.String(64), nullable=False)
    alamat = db.Column(db.String(256), nullable=True)
    agama = db.Column(db.String(32), nullable=True)
    mapel_id = db.Column(db.Integer, ForeignKey('tb_mapel.mapel_ID'), nullable=True)
    kelas_id = db.Column(db.Integer, ForeignKey('tb_kelas.kelas_ID'), nullable=True)
    
    def __init__(self, user_id, nip, nama_depan, nama_belakang, 
                 jenis_kelamin, alamat = None, agama = None, mapel_id = None, 
                 kelas_id = None) -> None:
        super().__init__()
        self.user_id = user_id
        self.nip = nip
        self.nama_depan = nama_depan    
        self.nama_belakang = nama_belakang
        self.jenis_kelamin = jenis_kelamin
        self.alamat = alamat
        self.agama = agama
        self.mapel_id = mapel_id
        self.kelas_id = kelas_id
        
    
    def __repr__(self) -> str:
        return '(id : {}, nama : {} {}, jenis_kelamin : {})'.format(self.guru_ID,
                                                                    self.nama_depan, self.nama_depan,
                                                                    self.jenis_kelamin)   