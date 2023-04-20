from flask_migrate import Migrate

from futmx import create_app, db
from futmx.accounts.models import User
from futmx.courses.models import Courses, Department, Lecturer, Question

app = create_app("development")

@app.shell_context_processor
def make_shell_ctx():
    """
    This function registers the application, database instances
    and models so that they automatically imported to shell.

    Auto imports app models to shell for easy testing.
    """
    return dict(
        app=app,
        db=db,
        User=User,
        Courses=Courses,
        Department=Department,
        Lecturer=Lecturer,
        Question=Question,
    )


if "__main__" == __name__:
    app.run(debug=True)
