from flask import request
from flask_restful import Resource
from Model import db, JobMonitor, JobMonitorSchema

monitoring_schema = JobMonitorSchema(many=True)
monitor_schema = JobMonitorSchema()


class MonitorResource(Resource):

    def get(self):
        monitor = JobMonitor.query.all()
        monitor = monitoring_schema.dump(monitor).data
        return {'status': 'success', 'data': monitor}, 200

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

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = monitor_schema.load(json_data)
        if errors:
            return errors, 422
        monitor = JobMonitor.query.filter_by(id=data['id']).first()
        if not monitor:
            return {'message': 'Job does not exist'}, 400
        monitor.app_name = data['app_name']
        db.session.commit()

        result = monitor_schema.dump(monitor).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = monitor_schema.load(json_data)
        if errors:
            return errors, 422
        monitor = JobMonitor.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = monitor_schema.dump(monitor).data

        return {"status": 'success', 'data': result}, 204

    @staticmethod
    def get_a_job(id):
        """
        Get a single job
        """
        monitor = JobMonitor.query.get(id)
        monitor = monitoring_schema.dump(monitor).data
        return {'status': 'success', 'data': monitor}, 200
