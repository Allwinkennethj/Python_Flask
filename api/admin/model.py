from common.base import Base
from config import db

class Admin_details(Base):
    __tablename__="Admin_details"

    username=db.Column(db.String(40),unique=True)
    name=db.Column(db.String(40))
    password=db.Column(db.String(100))

    def make_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}