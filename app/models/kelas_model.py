from app.extensions import db

class KelasModel(db.Model):
    __tablename__ = 'tb_kelas'
    kelas_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_kelas = db.Column(db.String(128), nullable=False)
    jml_siswa = db.Column(db.String(16), nullable=True)
    jml_laki = db.Column(db.String(16), nullable=True)
    jml_perempuan = db.Column(db.String(16), nullable=True)
    
    
    def __init__(self, nama_kelas, jml_siswa = None) -> None:
        super().__init__()
        self.nama_kelas = nama_kelas
        self.jml_siswa = jml_siswa
    
    def __repr__(self) -> str:
        return '(id : {}, nama_kelas : {}, jml_siswa : {})'.format(self.kelas_ID, self.nama_kelas, self.jml_siswa)