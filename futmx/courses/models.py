from futmx import db


class Courses(db.Model):

    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(64), unique=True)
    name = db.Column(db.UnicodeText(1000), nullable=False)
    year = db.Column(db.String(10))
    unit = db.Column(db.String(10))
    lecturers = db.relationship('Lecturer', backref='course') # backref adds a course attribute to other class models(imaginary)
    department = db.relationship('Department', backref='course')
    questions = db.relationship('Question', backref='course')

    def __repr__(self):
        return f'<{self.__class__.__name__}: "{self.name}...">'


class Lecturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.UnicodeText(1000), nullable=False)
    position = db.Column(db.String(200))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    def __repr__(self):
        return f'<{self.__class__.__name__}: "{self.name}...">'


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.UnicodeText(1000))
    faculty = db.Column(db.UnicodeText(1000))

    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    def __repr__(self):
        return f'<{self.__class__.__name__}: "{self.name}...">'


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
        return f'<{self.__class__.__name__}: "{self.question_text[0:20]}...">'
