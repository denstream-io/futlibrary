######   Routes for login/logout/signup/forgot password ####


from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from .forms import RegistrationForm, LoginForm, CourseSelectionForm
from .models import (User, AcademicInfo,) # FacultyDepartmentDropDown)
from flask_login import login_user, current_user, logout_user, login_required


from futmx import db, bcrypt

# Initializing Home Blueprint
home = Blueprint("home", __name__)


@home.route("/")
def index():
    return render_template("account/index.html")


@home.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
        #     "utf-8"
        # )
        user = User(
            username=form.username.data, email=form.email.data.lower(), password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You are now able to log in", "success")
        return redirect(url_for("home.login"))
    return render_template("account/register.html", title="Register", form=form)


@home.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.is_correct_password(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home.index"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("account/login.html", title="Login", form=form)


@login_required
@home.route("/academia", methods=["GET", "POST"])
def academic_info():
    form = CourseSelectionForm()
    if form.validate_on_submit():
        academia = AcademicInfo(
            faculty=form.faculty.data,
            level=form.level.data,
            courses=form.courses.data,
            department=form.department.data,
        )
        db.session.add(academia)
        db.session.commit()
        return redirect(url_for("home.index"))
    return render_template("account/academia.html", title="Academia", form=form)


@home.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))
