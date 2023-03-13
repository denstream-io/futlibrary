######   Routes for login/logout/signup/forgot password ####


from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from .forms import RegistrationForm, LoginForm
from .models import User
from flask_login import login_user, current_user, logout_user, login_required


from futmx import db, bcrypt

# Initializing home_bp Blueprint
home_bp = Blueprint("home_bp", __name__)


@home_bp.route("/")
def index():
    return render_template("account/index.html")


@home_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home_bp"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data, email=form.email.data.lower(), password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You are now able to log in", "success")
        return redirect(url_for("home_bp.login"))
    return render_template("account/register.html", title="Register", form=form)


@home_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home_bp"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.is_correct_password(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home_bp.index"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("account/login.html", title="Login", form=form)





@home_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home_bp"))
