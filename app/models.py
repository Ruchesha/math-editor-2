from . import db

class MathOperation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operation = db.Column(db.String(50), nullable=False)
    value1 = db.Column(db.Float, nullable=False)
    value2 = db.Column(db.Float, nullable=False)
    result = db.Column(db.Float, nullable=False)
