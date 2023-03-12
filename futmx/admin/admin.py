

from flask import Blueprint
from futmx import admin, db
from ..accounts.models import User

# from flask_admin.contrib.sqla import 
from .models import (UserView, CoursesView, DepartmentView, LecturerView, QuestionView)
from ..courses.models import (Courses, Lecturer, Department, Question)


admin_bp = Blueprint('admin_bp', __name__)

admin.add_view(UserView(User, db.session))
admin.add_view(CoursesView(Courses, db.session))
admin.add_view(LecturerView(Lecturer, db.session))
admin.add_view(DepartmentView(Department, db.session))
admin.add_view(QuestionView(Question, db.session))






