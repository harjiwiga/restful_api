from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    get_current_user

)

from myapi.models.report import Report, ReportType
from myapi.extensions import ma, db
from myapi.commons.pagination import paginate


# current_user = get_jwt_identity()

class ReportSchema(ma.ModelSchema):
    class Meta:
        model = Report
        sqla_session = db.session


class ReportTypeSchema(ma.ModelSchema):
    class Meta:
        model = ReportType
        sqla_session = db.session


class ReportResource(Resource):
    method_decorators = [jwt_required]

    def get(self, Report):
        schema = ReportSchema()


class ReportTypeResource(Resource):
    method_decorators = [jwt_required]

    def get(self):
        schema = ReportTypeSchema(many=True)
        user = get_current_user()
        report_types = ReportType.query.all()
        return schema.dump(report_types).data


class ReportList(Resource):
    method_decorators = [jwt_required]

    def get(self):
        schema = ReportSchema(many=True)
        user = get_current_user()
        # reports = Report.query.filter_by(users = )
