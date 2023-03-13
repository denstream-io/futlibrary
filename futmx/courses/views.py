from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required
from .forms import CourseSelectionForm
from .models import RegisterCourse

from futmx import db

course_bp = Blueprint('course_bp', __name__)



@login_required
@course_bp.route("/register_courses", methods=["GET", "POST"])
def register_courses():
    form = CourseSelectionForm()
    if form.validate_on_submit():
        academia = RegisterCourse(
            courses=form.courses.data
        )
        db.session.add(academia)
        db.session.commit()
        return redirect(url_for("home.index")) # bug
    return render_template("courses/register_courses.html", title="Academia", form=form)