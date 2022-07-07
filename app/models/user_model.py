from app.extensions import db 
from app.lib.custome.time_zone import utc_makassar
from sqlalchemy.dialects.mysql import SMALLINT, INTEGER, VARCHAR
from sqlalchemy import Column, ForeignKey, null
from app.extensions import bcrypt

class UserModel(db.Model):
    __tablename__ = 'tb_user'
    ID = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    group = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(128), nullable=True)
    activation_code = db.Column(db.String(64), nullable=True)
    create_on = db.Column(db.DateTime, default=utc_makassar())
    last_login = db.Column(db.DateTime, onupdate=utc_makassar())
    active = Column(SMALLINT, nullable=True)

    def __init__(self, username, group, password, email) -> None:
        self.username = username
        self.group = group
        self.password = bcrypt.generate_password_hash(password)
        self.email = email
        self.active = 1
        
    def __repr__(self) -> str:
        return '[(id: {}, username: {})]'.format(self.ID, self.username)

    def check_pw_hash(*args, **kwargs):
        return bcrypt.check_password_hash(*args, **kwargs)

    def generate_pw_hash(password):
        return bcrypt.generate_password_hash(password)


class UserDetailModel(db.Model):
    __tablename__ = 'tb_user_detail'
    user_detail_ID = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    user_id = Column(INTEGER(unsigned=True), ForeignKey('tb_user.ID'), nullable=False)
    nama_depan = Column(VARCHAR(128), nullable=False)
    nama_belakang = Column(VARCHAR(128), nullable=False)
    jenis_kelamin = Column(VARCHAR(32), nullable=False)
    alamat = Column(VARCHAR(256), nullable=False)
    telp = Column(VARCHAR(13), nullable=True)
    profil_picture = Column(VARCHAR(256), nullable=True)

    def __init__(self, user_id, nama_depan, nama_belakang, jenis_kelamin, alamat, telp) -> None:
        self.user_id = user_id
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.jenis_kelamin = jenis_kelamin
        self.alamat = alamat
        self.telp = telp

    def __repr__(self) -> str:
        return '[(user_detail_ID: {}, user_id : {}, nama depan: {}, nama belakang: {})]' \
                .format(self.user_detail_ID, self.user_id, self.nama_depan, self.nama_belakang)
    


