from flask_jwt_extended import (
    jwt_required,
    get_current_user

)
from flask_restful import Resource
from geoalchemy2 import func

from myapi.api.resources.converter import GeoConverter
from myapi.extensions import ma, db
from myapi.models.report import Report, ReportType
from flask import request


# current_user = get_jwt_identity()

class ReportSchema(ma.ModelSchema):
    class Meta:
        model = Report
        sqla_session = db.session
        model_converter = GeoConverter


class ReportTypeSchema(ma.ModelSchema):
    class Meta:
        model = ReportType
        sqla_session = db.session


class ReportResource(Resource):
    method_decorators = [jwt_required]
    schema = ReportSchema()

    def get(self):
        user = get_current_user()
        return {"reports": self.schema.dump(user.get_reports()).data}, 201

    def get(self, current_geo_location):
        reports = Report.query.filter_by(func.ST_Distance(Report.location, current_geo_location) < 100)

        return {"reports": self.schema.dump(reports).data}

    def post(self):
        schema = ReportSchema()
        report, errors = schema.load(request.json)
        if errors:
            return errors, 422

        db.session.add(report)
        db.session.commit()

        return {"msg": "report created", "user": schema.dump(report).data}, 201



class ReportTypeResource(Resource):
    method_decorators = [jwt_required]

    def get(self):
        schema = ReportTypeSchema(many=True)
        report_types = ReportType.query.all()
        return schema.dump(report_types).data


class Reports(Resource):
    method_decorators = [jwt_required]

    def get(self):
        schema = ReportSchema(many=True)
        user = get_current_user()

        # reports = Report.query.filter_by(users = )
