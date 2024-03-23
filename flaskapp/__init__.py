from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
app.config['SECRET_KEY'] = '0c2608d46f12480aba8837cf2807454a'
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# initialize the app with the extension
bcrypt = Bcrypt(app)
db.init_app(app)

app.app_context().push()

with app.app_context():
    db.create_all()

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskapp import routes