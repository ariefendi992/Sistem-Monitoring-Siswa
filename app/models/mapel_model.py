from app.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import INTEGER

class MapelModel(db.Model):
    __tablename__ = 'tb_mapel'
    mapel_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mapel = db.Column(db.String(128), nullable=False)
    
    def __init__(self, mapel):
        self.mapel = mapel
        
    def __repr__(self) -> str:
        return '(id : {}, mapel {})'.format(self.mapel_ID, self.mapel)

class JadwalMapel(db.Model):
    __tablename__ = 'tb_jadwal_belajar'
    jadwal_belajar_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    siswa_id = db.Column(INTEGER(unsigned=True), db.ForeignKey('tb_siswa_detail.siswa_ID'),)
    mapel_id = db.Column(db.Integer, db.ForeignKey('tb_mapel.mapel_ID'), nullable=False)
    hari = db.Column(db.String(32), nullable=False)
    jam_mulai = db.Column(db.String(32), nullable=False)
    jam_selesai = db.Column(db.String(32), nullable=False)
    kelas_id = db.Column(db.Integer, ForeignKey('tb_kelas.kelas_ID'), nullable=True)
    
    def __init__(self, student_id, mapel_id, day, start, end, class_id) -> None:
        super().__init__()
        self.siswa_id = student_id
        self.mapel_id = mapel_id
        self.hari = day
        self.jam_mulai = start
        self.jam_selesai = end
        self.kelas_id = class_id
        
    def __repr__(self) -> str:
        return 'id : {}, mapel : {},  hari : {}, mulai : {}, selesai : {}, kelas id: {}'\
                .format(self.jadwal_belajar_ID, self.mapel_id, self.hari, self.jam_mulai,
                   self.jam_selesai, self.kelas_id)
    