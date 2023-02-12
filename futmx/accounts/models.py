
from futmx import db, login_manager
from datetime import datetime
from flask_login import UserMixin


# TODO
    # INSTALL FLASK
    # INSTALL FLASK-SQLALCHEMY
    # FIND LENGHT OF LONGEST NAME IN THE WORLD
    # SEARCH THE FACULTIES AND COURSES IN FUTMINNA
    # ASK BERNARD

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False) # Two types of Admin
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return self.__class__.__name__ + '(' + self.username + ',' + self.email + ')'

class AcadInfo(db.Model, User):

    def __init__(self) -> None:
        super().__init__()
    

    faculty = db.Column(db.String(64), unique=True)
    ...

