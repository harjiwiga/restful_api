from myapi.extensions import db

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_type_id = db.Column(db.Integer,db.ForeignKey("report_type.id"))

    def __init__(self,**kwargs):
        super(User, self).__init__(**kwargs)

    

class ReportType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
