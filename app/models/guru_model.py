from app.extensions import db   
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import ForeignKey

class GuruModel(db.Model):
    __tablename__ = 'tb_guru_detail'
    guru_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # user_id = db.Column(INTEGER(unsigned=True), ForeignKey('tb_user.ID'), nullable=False)
    nip = db.Column(db.String(32), nullable=False)
    nama_guru = db.Column(db.String(128), nullable=False)
    jenis_kelamin = db.Column(db.String(64), nullable=False)
    alamat = db.Column(db.String(256), nullable=True)
    agama = db.Column(db.String(32), nullable=True)