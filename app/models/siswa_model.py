from app.extensions import db
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

class SiswaModel(db.Model):
    __tablename__ = 'tb_siswa_detail'
    siswa_ID = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    user_id = Column(INTEGER(unsigned=True), ForeignKey('tb_user.ID', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    nama_depan = Column(VARCHAR(64), nullable=False)
    nama_belakang = Column(VARCHAR(64), nullable=False)
    nisn = db.Column(db.String(32), nullable=False)
    tempat_lahir = db.Column(db.String(64), nullable=True)
    tanggal_lahir = db.Column(db.String(64), nullable=True)
    jenis_kelamin = db.Column(db.String(32), nullable=True)
    agama = db.Column(db.String(32), nullable=True)
    alamat = db.Column(db.String(256), nullable=True)
    foto_siswa = db.Column(db.String(256), nullable=True)
    kelas_id = db.Column(db.Integer, ForeignKey('tb_kelas.kelas_ID', ondelete='CASCADE'), nullable=True)
    qr_code = db.Column(db.String(256), nullable=True)


    def __init__(self, user_id, nama_depan, nama_belakang, nisn, jk = None, agama=None, alamat=None, kelas_id=None) -> None:
        self.user_id = user_id
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nisn = nisn
        self.jenis_kelamin = jk
        self.agama = agama
        self.alamat = alamat
        self.kelas_id = kelas_id



