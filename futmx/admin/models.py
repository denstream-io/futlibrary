from flask_admin.contrib.sqla import ModelView

class UserView(ModelView):
    # Setting user table constraints on admin
    can_delete = False
    column_exclude_list = ['_password']
    column_display_pk = True

class CoursesView(ModelView):
    # column_hide_backrefs = False
    can_delete = False
    column_list = ['lecturers', 'department', 'questions']

class DepartmentView(ModelView):
    ...
class QuestionView(ModelView):
    ...
class LecturerView(ModelView):
    ...