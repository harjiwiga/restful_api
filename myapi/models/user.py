from myapi.extensions import db, pwd_context
from myapi.models.role import Role
from myapi.models.table_name import TableName

# from myapi.models.report import Report

users_roles = db.Table(
    'users_roles',
    db.Column('user_id', db.Integer, db.ForeignKey(TableName.USER + '.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)


class UserType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)

    def __init__(self, **kwargs):
        super(UserType, self).__init__(**kwargs)

    def __repr__(self):
        return "<UserType %s>" % self.name


class User(db.Model):
    """Basic user model
    """
    __tablename__ = TableName.USER
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_type.id'))
    user_type = db.relationship(UserType,
                                primaryjoin=
                                user_type_id == UserType.id,
                                post_update=True)
    roles = db.relationship(
        Role,
        secondary=users_roles,
        backref=db.backref('roles', lazy='dynamic')
    )

    reports = db.relationship("Report", backref=db.backref("user_reporter"))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = pwd_context.hash(self.password)

    def __repr__(self):
        return "<User %s>" % self.username

    def add_role(self, role):
        self.roles.append(role)

    def add_roles(self, roles):
        for role in roles:
            self.add_role(role)

    def get_roles(self):
        for role in self.roles:
            yield role

    def get_reports(self):
        return self.reports