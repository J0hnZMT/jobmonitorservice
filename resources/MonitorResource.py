from flask import request
from flask_restful import Resource
from resources.Model import db, JobMonitor, JobMonitorSchema

monitoring_schema = JobMonitorSchema(many=True)
monitor_schema = JobMonitorSchema()


class MonitorApi(Resource):

    def get(self, job_id):
        data = {"id": job_id}
        if job_id.isdigit():
            monitor = JobMonitor.query.filter_by(id=data['id'])
        else:
            monitor = JobMonitor.query.filter_by(job_id=data['id'])
        result = monitoring_schema.dump(monitor).data
        return {'status': 'success', 'data': result}, 200

    def put(self, job_id):
        search_data = {"id": job_id}
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = monitor_schema.load(json_data)
        if errors:
            return errors, 422
        monitor = JobMonitor.query.filter_by(id=search_data['id']).first()
        if not monitor:
            return {'message': 'Job does not exist'}, 400
        # monitor.app_name = data['app_name']
        monitor.state = data['state']
        db.session.commit()
        result = monitor_schema.dump(monitor).data
        return {"status": 'success', 'data': result}, 200

    def delete(self, job_id):
        data = {"id": job_id}
        JobMonitor.query.filter_by(id=data['id']).delete()
        db.session.commit()
        return {"status": 'success', "message":'id:{} deleted'.format(data['id'])}, 200


class MonitorList(Resource):

    def get(self):
        monitor = JobMonitor.query.all()
        result = monitoring_schema.dump(monitor).data
        return {'status': 'success', 'data': result}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = monitor_schema.load(json_data)
        if errors:
            return errors, 422
        monitor = JobMonitor.query.filter_by(app_name=data['app_name']).first()
        if monitor:
            return {'message': 'Job already exists'}, 400
        monitor = JobMonitor(
            job_id=json_data['job_id'],
            app_name=json_data['app_name'],
            state=json_data['state'],
            date_created=json_data['date_created']
        )
        db.session.add(monitor)
        db.session.commit()
        result = monitor_schema.dump(monitor).data
        return {"status": 'success', 'data': result}, 201
