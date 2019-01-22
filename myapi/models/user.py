from myapi.extensions import db, pwd_context

class User(db.Model):
    """Basic user model
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_type.id'))

    
    
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = pwd_context.hash(self.password)

    def __repr__(self):
        return "<User %s>" % self.username
    
    
class UserType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60),unique=True, nullable=False)
    
    def __init__(self,**kwargs):
        super(UserType,self).__init__(**kwargs)

    def __repr__(self):
        return "<UserType %s>" %self.name