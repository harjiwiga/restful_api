from flask_rbac import RoleMixin
from myapi.extensions import db

# roles_parents = db.Table(
#     'roles_parents',
#     db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
#     db.Column('parent_id', db.Integer, db.ForeignKey('role.id'))
# )


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name):
        RoleMixin.__init__(self)
        self.name = name

    @staticmethod
    def get_by_name(name):
        return Role.query.filter_by(name=name).first()