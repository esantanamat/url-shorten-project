from db import db
from datetime import datetime
from sqlalchemy.sql import func

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.Text, nullable=False)
    short_url = db.Column(db.String(40), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())  
    updated_at = db.Column(db.DateTime, onupdate=func.now()) 
    access_count = db.Column(db.Integer, default=0)
