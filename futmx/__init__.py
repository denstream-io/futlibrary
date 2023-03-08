##### Initialization of Application
#### Application Package Constructor

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

#from .config import config



db = SQLAlchemy()
login_manager = LoginManager()

# Constructor not initialized with application yet
bcrypt = Bcrypt() 

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


    # Registering the blueprints
    from .accounts import views
    app.register_blueprint(views.home)

    return app

# Running App as a whole
# app = create_app('development')

# if __name__ == '__main__':
#     app.run(debug=True)
    