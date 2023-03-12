##### Initialization of Application
#### Application Package Constructor

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
from flask_migrate import Migrate


# Unintialized Constructors
db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt() 
admin = Admin(name='futlibrary', template_mode='bootstrap3')
migrate = Migrate()

def create_app(config_type):
    app = Flask(__name__)

    from config import config

    app.config.from_object(config[config_type])
    config[config_type].init_app(app)

    # Initilizing Application
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    migrate.init_app(app, db)
    admin.init_app(app)

    
    # Registering the blueprints
    from .accounts import views
    from .admin import admin_bp
    app.register_blueprint(admin_bp)
    app.register_blueprint(views.home)

    return app
