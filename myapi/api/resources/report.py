# from flask import request
# from flask_restful import Resource
# from flask_jwt_extended import jwt_required
#
# from myapi.models import Report
# from myapi.extensions import ma, db
# from myapi.commons.pagination import paginate
#
# class ReportSchema(ma.ModelSchema):
#     class Meta:
#         model = Report
#         sqla_session = db.session
#
# class ReportResource(Resource):
#     method_decorators = [jwt_required]
#
