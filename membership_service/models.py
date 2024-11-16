# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer)  # Assume this links to the Member's ID
    start_date = db.Column(db.String(10))
    expiry_date = db.Column(db.String(10))

    def to_dict(self):
        return {
            'id': self.id,
            'member_id': self.member_id,
            'start_date': self.start_date,
            'expiry_date': self.expiry_date
        }