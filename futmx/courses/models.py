from futmx import db
# from ..accounts.models import User
from sqlalchemy.ext.declarative import declared_attr

class Courses(db.Model):

    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(64), unique=True)
    name = db.Column(db.UnicodeText(1000), nullable=False)
    year = db.Column(db.String(10))
    unit = db.Column(db.String(10))
    # Line 14: backref adds a course attribute to other class models(imaginary)
    lecturers = db.relationship('Lecturer', backref='course') 
    department = db.relationship('Department', backref='course')
    questions = db.relationship('Question', backref='course')

    @declared_attr
    def users_id(cls):
        return db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<{self.__class__.__name__}: '{self.name}'>"


class Lecturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.UnicodeText(1000), nullable=False)
    position = db.Column(db.String(200))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    def __repr__(self):
        return f"<{self.__class__.__name__}: '{self.name}'>"


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.UnicodeText(1000))
    faculty = db.Column(db.UnicodeText(1000))

    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    def __repr__(self):
        return f"<{self.__class__.__name__}: '{self.name}'>"


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    option_A = db.Column(db.String(200))
    option_B = db.Column(db.String(200))
    option_C = db.Column(db.String(200))
    option_D = db.Column(db.String(200))
    solution = db.Column(db.Text)
    question_image_link = db.Column(db.Text)
    question_text = db.Column(db.UnicodeText(1000), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    def __repr__(self):
        return f"<{self.__class__.__name__}: '{self.id}'>"


class RegisterCourse(db.Model):

    # def __init__(self) -> None:
    #     super().__init__()
    __abstract__ = True
    # courses = db.Column(db.String(64))
    @declared_attr
    def courses(cls):
        return db.relationship('Courses', primaryjoin=lambda: cls.id == Courses.users_id, backref='user')
