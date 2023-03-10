from futmx import db


class Courses(db.Model):

    __tablename__ = "courses"

    code = db.Column(db.String(64), unique=True, primary_key=True)
    name = db.Column(db.UnicodeText(1000), nullable=False)
    lecturers = db.relationship('Lecturer', backref='post')
    department = db.relationship('Department', backref='post')
    year = db.Column(db.String(10))
    questions = db.relationship('Question', backref='post')
    unit = db.Column(db.String(10))


class Lecturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.UnicodeText(1000), nullable=False)
    position = db.Column(db.String(200))

    def __repr__(self):
        return f'<Lecturer: "{self.name}...">'


class Department(db.Model):
    name = db.Column(db.UnicodeText(1000), primary_key=True)
    faculty = db.Column(db.UnicodeText(1000))

    def __repr__(self):
        return f'<Department: "{self.name}...">'


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.UnicodeText(1000), nullable=False)
    question_image_link = db.Column(db.Text)
    option_A = db.Column(db.String(200))
    option_B = db.Column(db.String(200))
    option_C = db.Column(db.String(200))
    option_D = db.Column(db.String(200))
    solution = db.Column(db.Text)

    def __repr__(self):
        return f'<Question: "{self.question_text[0:20]}...">'
