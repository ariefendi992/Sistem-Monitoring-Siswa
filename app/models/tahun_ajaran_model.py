from app.extensions import db 

class TahunAjaranModel(db.Model):
    __tablename__ = 'tb_tahun_ajaran'
    tahun_ajaran_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tahun_ajaran = db.Column(db.String(32), nullable=False)
    status = db.Column(db.String(2), nullable=False)
    
    def __init__(self, tahun_ajaran) -> None:
        super().__init__()
        self.tahun_ajaran = tahun_ajaran
        self.status = 1
        
    def __repr__(self) -> str:
        return '[(id : {}, tahun_ajaran : {}, status : {})]'.format(self.tahun_ajaran_ID,
                                                                    self.tahun_ajaran, self.status)
