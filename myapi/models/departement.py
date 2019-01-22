from myapi.extensions import db

class Departement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), unique=True)
    address = db.Column(db.String(90))
    longitude = db.Column(db.Float())
    latitude = db.Column(db.Float())
    report_type_id = db.Column(db.Integer, db.ForeignKey('report_type.id')) 
    
    def __init__(self,**kwargs):
        super(Departement, self).__init__(**kwargs)
        
    def __repr__(self):
        return "<Departement %s>" % self.name