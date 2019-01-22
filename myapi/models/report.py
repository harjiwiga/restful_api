from myapi.extensions import db


report_user_table = db.Table('report_user_table',db.metadata,
                             db.Column('report_id', db.Integer, db.ForeignKey('report.id')),
                             db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
                             )


class Report(db.Model):
    __tablename__ = 'report'
    id = db.Column(db.Integer, primary_key=True)
    report_type_id = db.Column(db.Integer, db.ForeignKey("report_type.id"))
    datetime = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Integer,db.ForeignKey("status.id"))
    address = db.Column(db.String(120))
    longitude = db.Column(db.Float(), default=0)
    latitude = db.Column(db.Float(),  default=0)
    radius = db.Column(db.Float(), default=0)
    users = db.relationship("User", secondary = report_user_table, backref=db.backref("reports", lazy="dynamic"), lazy= "dynamic")
    update_status_time = db.Column(db.DateTime, nullable=False)
    
    def __init__(self,**kwargs):
        super(Report, self).__init__(**kwargs)


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    def __init__(self, **kwargs):
        super(Status, self).__init__(**kwargs)


class ReportType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)

    def __init__(self,**kwargs):
        super(ReportType,self).__init__(**kwargs)