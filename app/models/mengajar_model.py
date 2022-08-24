from app.extensions import db
class MengajarModel(db.Model):
    __tablename__ = 'tb_mengajar'
    mengajar_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    kode_mengajar = db.Column(db.String(128), nullable=False)
    hari = db.Column(db.String(32), nullable=False)
    mulai = db.Column(db.String(12), nullable=False)
    selesai = db.Column(db.String(12), nullable=False)
    guru_id = db.Column(db.Integer, nullable=False)
    mapel_id = db.Column(db.Integer, nullable=False)
    kelas_id = db.Column(db.Integer, nullable=False)
    semester_id = db.Column(db.Integer, nullable=False)
    th_ajaran_id = db.Column(db.Integer, nullable=False)
    
    
    def __init__(self, kd_menghajar, hari, jam_mulai, jam_selesai, guru_id, mapel_id, kelas_id, sms_id, ta_id) -> None:
        self.kode_mengajar = kd_menghajar
        self.hari = hari
        self.mulai = jam_mulai
        self.selesai = jam_selesai
        self.guru_id = guru_id
        self.mapel_id = mapel_id
        self.kelas_id = kelas_id
        self.semester_id = sms_id
        self.th_ajaran_id = ta_id
        
    def __repr__(self) -> str:
        return 'id : {}, kode_mapel : {}'.format(self.mengajar_ID, self.kode_mengajar)