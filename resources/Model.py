from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID


ma = Marshmallow()
db = SQLAlchemy()


class JobMonitor(db.Model):
    __tablename__ = 'monitor'
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(UUID(as_uuid=True), nullable=False)
    app_name = db.Column(db.String(150), nullable=False)
    state = db.Column(db.String(10), nullable=False)
    date_created = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, job_id, app_name, state, date_created):
        self.job_id = job_id
        self.app_name = app_name
        self.state = state
        self.date_created = date_created


class JobMonitorSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    job_id = fields.UUID(dump_only=True)
    app_name = fields.String(validate=validate.Length(1))
    state = fields.String(validate=validate.Length(1))
    date_created = fields.DateTime()
