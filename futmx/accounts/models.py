
from futmx import db, login_manager, bcrypt
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    _password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False) # Two types of Admin
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    send_email = db.Column(db.Boolean, nullable=False, default=False) # for opt in news letters
    email_confirmed = db.Column(db.Boolean, nullable=False, default=False) # for confirming legit emails


    @hybrid_property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = bcrypt.generate_password_hash(value)
    
    def is_correct_password(self, plaintext):
        """Check password."""
        return bcrypt.check_password_hash(self.password, plaintext)

    def __repr__(self):
        return self.__class__.__name__ + '(' + self.username + ',' + self.email + ')'


class AcademicInfo(User):

    def __init__(self) -> None:
        super().__init__()
    

    faculty = db.Column(db.String(64))
    department = db.Column(db.String(64))
    level = db.Column(db.String(64))
    courses = db.Column(db.String(64))



