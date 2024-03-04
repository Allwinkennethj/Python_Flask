from uuid import uuid4
from datetime import datetime,timezone
from config import db

class Base(db.Model):
    __abstract__=True

    id=db.Column(db.String(40),default=uuid4,primary_key=True)
    created_on=db.Column(db.DateTime,default=datetime.now(timezone.utc))
    updated_on=db.Column(db.DateTime,onupdate=datetime.now(timezone.utc))
    created_by=db.Column(db.String(40))
    updated_by=db.Column(db.String(40))