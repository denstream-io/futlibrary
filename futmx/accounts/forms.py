from flask_wtf import FlaskForm
#from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import (User,)# FacultyDepartmentDropDown)
from .utils import MultiCheckboxField


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')]) # Must be equal to Password field
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """
        Ensures User username are unique
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        """
        Ensures users Email are unique
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me') # A remember me field
    submit = SubmitField('Login')


class RequestResetForm(FlaskForm):
    """
    A form used for email reset
    """
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    """
    A form used for password reset
    """
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class CourseSelectionForm(FlaskForm):
    """
    A form used for selecting offered courses
    for the app
    """

    faculty = SelectField('Faculty', choices=[] )
    department = SelectField('Department')
    level = SelectField("Level", choices=['100lvl', '200lvl', '300lvl', '400lvl', '500lvl']) 
    courses = MultiCheckboxField('Courses', choices = ['foo', 'bar', 'baz'])

