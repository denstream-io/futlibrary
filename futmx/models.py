
from futmx import db
from datetime import datetime


# TODO
    # INSTALL FLASK
    # INSTALL FLASK-SQLALCHEMY
    # FIND LENGHT OF LONGEST NAME IN THE WORLD
    # SEARCH THE FACULTIES AND COURSES IN FUTMINNA
    # ASK BERNARD

class User(db.Model):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False) # Two types of Admin
    created_at = db.Column(db.DateTime, nullable=False, default=False)
    updated_at = db.Column(db.DateTime, nullable=False, default=False)

    # Three things that are not user specific(This option should display on drop down menu)

    faculty = db.Column(db.String(64), nullable=False) # Makes courses easy to locate
    department = db.Column(db.String(150), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    courses = db.Column(db.String(120), nullable=True)
    paper = db.relationship('Paper', backref='user', uselist=False) # One to One relationship with Paper Model

    def __repr__(self):
        return self.__class__.__name__ + '(' + self.username + ',' + self.email + ')'

class Paper(db.Model):

    "A paper will have many questions"
    "A one to many relationship with Question Model"

    __tablename__ = 'papers'
    id = db.Column(db.Integer, primary_key=True)
    # duration = db.Column(datetime.timedelta, nullable=False) # Pending information
    description = db.Column(db.Text, nullable=True)
    paper_type = db.Column(db.String(64), nullable=False)

    # You wnat to select from different data tables based on the course_code
    # instead of having a model for each course

    course_code = db.Column(db.String(64), nullable=False)
    questions = db.relationship('Question', backref='questions')
    paper_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __repr__(self):
        return self.__class__.__name__ + '(' + self.username + ',' + self.email + ')'

    


class Question(db.Model):

    "Question model should query database table for questions"

    __tablename__= 'questions'

    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Unicode(1000), nullable=False)
    options = db.Column(db.Unicode(1000), nullable=False) # Still wondering how it would be parsed on the views
    questions = db.Column(db.UnicodeText(1000), nullable=False)
    year = db.Column(db.String(64), nullable=True)
    question_id = db.Column(db.Integer, db.ForeignKey('papers.id'))

    def __repr__(self):
        return self.__class__.__name__ + '(' + self.year  + ')'




    
