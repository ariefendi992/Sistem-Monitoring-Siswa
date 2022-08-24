from app.extensions import db
from sqlalchemy import and_, select, tuple_

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

    def fetch_join_all(self, *args):
        return db.session.query(self.table,*args).join(*args)
        # return self.table.query.join(*args, **kwargs).all()
        
    def join_without_fk(self, tb_join = (), filter = []):
        tb_join = tb_join
        tb_filter = filter     
        return db.session.query(self.table).add_entity(tb_join).join(tb_join, tb_filter)
        # print(tb_join)

    def limit_one(self,*args, **kwargs):
        return self.table.query.filter(*args, **kwargs).order_by(**kwargs).limit(1).all()
