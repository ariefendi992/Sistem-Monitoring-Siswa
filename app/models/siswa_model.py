from app.extensions import db
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

class SiswaModel(db.Model):
    __tablename__ = 'tb_siswa_detail'
    siswa_ID = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    user_id = Column(INTEGER(unsigned=True), ForeignKey('tb_user.ID'), nullable=False)
    nama_siswa = Column(VARCHAR(64), nullable=False)
    nisn = db.Column(db.String(32), nullable=False)
    tempat_lahir = db.Column(db.String(64), nullable=True)
    tanggal_lahir = db.Column(db.String(64), nullable=True)
    jenis_kelamin = db.Column(db.String(32), nullable=False)
    agama = db.Column(db.String(32), nullable=False)
    alamat = db.Column(db.String(256), nullable=True)
    nama_ayah = db.Column(db.String(128), nullable=True)
    nama_ibu = db.Column(db.String(128), nullable=True)
    foto_siswa = db.Column(db.String(256), nullable=True)


    def __init__(self, user_id, nama_siswa, nisn, jk, agama) -> None:
        self.user_id = user_id
        self.nama_siswa = nama_siswa
        self.nisn = nisn
        self.jenis_kelamin = jk
        self.agama = agama



