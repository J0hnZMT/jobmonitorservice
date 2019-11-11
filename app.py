from flask import Blueprint, Flask
from flask_restful import Api
from resources.MonitorResource import MonitorApi, MonitorList

app = Flask(__name__)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(MonitorList, '/')
api.add_resource(MonitorApi, '/<job_id>')


