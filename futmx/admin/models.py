from flask_admin.contrib.sqla import ModelView

class UserView(ModelView):
    # Setting User table constraints on admin
    can_delete = False
    column_exclude_list = ['_password']
    column_display_pk = True
    column_list = ['id','username', 'email', 'courses', 'faculty', 'department', 'level' ]

class CoursesView(ModelView):
    # Setting Courses table constraints on admin
    can_delete = False
    column_list = ['id', 'code', 'name', 'year', 'unit', 'lecturers', 'department', 'questions']

class DepartmentView(ModelView):
    ...
class QuestionView(ModelView):
    ...
class LecturerView(ModelView):
    ...