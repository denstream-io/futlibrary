
from futmx import admin, db

from ..courses.models import (Courses, Lecturer, Department, Question)
from ..accounts.models import (User)

from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):
    # Setting user table constraints on admin
    can_delete = False

class CoursesView(ModelView):
    ...
class DepartmentView(ModelView):
    ...
class QuestionView(ModelView):
    ...
class UserView(ModelView):
    ...

# Add  administrative views here
admin.add_view(UserView(User, db.session))
admin.add_view(ModelView(Lecturer, db.session))
admin.add_view(ModelView(Courses, db.session))
admin.add_view(ModelView(Department, db.session))
admin.add_view(ModelView(Question, db.session))




