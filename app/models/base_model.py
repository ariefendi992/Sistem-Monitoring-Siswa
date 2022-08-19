from app.extensions import db

class BaseModel:
    def __init__(self, table) -> None:
        self.table = table

    def  insert_data(self):
        data = self.table
        db.session.add(data)
        db.session.commit()

    def update_data(self):
        return db.session.commit()

    def delete_data(self, *args):      
        db.session.delete(*args)
        db.session.commit()

    def fetch_all(self):
        return self.table.query.all()

    def filter_by(self, **kwargs):
        return self.table.query.filter_by(**kwargs).first()

    def fetch_join_all(self,**kwargs):
        return db.session.query(self.table,**kwargs).join(**kwargs).all()
        # return self.table.query.join(*args, **kwargs).all()

    def limit_one(self,**kwargs):
        return self.table.query.filter(*args, **kwargs).order_by(**kwargs).limit(1).all()
