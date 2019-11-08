from flask import request, json, Response, Blueprint
from ..Model import JobMonitor, JobMonitorSchema

job_api = Blueprint('modulelogs', __name__)
job_schema = JobMonitorSchema()