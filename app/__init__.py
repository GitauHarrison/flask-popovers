from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_migrate import Migrate
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
moment = Moment(app)
migrate = Migrate(app, db, render_as_batch=True)

from app import routes, errors, models
