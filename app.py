from flask import Blueprint, Flask
from flask_restful import Api
from resources.Monitor import MonitorResource
from Model import JobMonitor, JobMonitorSchema

app = Flask(__name__)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(MonitorResource, '/modulelogs/index')


@app.route('/<int:pk_id>', methods=['GET'])
def get_a_job(pk_id):
    """
    Get a single job
    """
    MonitorResource.get_a_job(pk_id)

