from app.extensions import db

class SemesterModel(db.Model):
    __tablename__ = 'tb_semester'
    semester_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    semester = db.Column(db.String(32), nullable=False)
    status = db.Column(db.String(2), nullable=False)
    
    def __init__(self, semester) -> None:
        super().__init__()
        self.semester = semester
        self.status = 1
        
    def __repr__(self) -> str:
        return '[(id : {}, semester : {}, status : {})]'.format(self.semester_ID, self.semester, self.status)