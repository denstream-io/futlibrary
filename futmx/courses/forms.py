from .utils import MultiCheckboxField
from wtforms import SelectField
from flask_wtf import FlaskForm



class CourseSelectionForm(FlaskForm):
    """
    A form used for selecting offered courses
    for the app
    """

    faculty = SelectField('Faculty', choices=['SEET'] )
    department = SelectField('Department', choices=['EEE'])
    level = SelectField("Level", choices=['100lvl', '200lvl', '300lvl', '400lvl', '500lvl']) 
    courses = MultiCheckboxField('Courses', choices = ['foo', 'bar', 'baz'])