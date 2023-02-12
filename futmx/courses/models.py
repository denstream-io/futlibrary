from futmx import db

class Courses(db.Model):

    __tablename__ = "courses"

    course_code = db.Column(db.String(64), unique=True)
    questions = db.Column(db.UnicodeText(1000), nullable=False)
    answer = db.COlumn()