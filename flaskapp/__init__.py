from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


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

from flaskapp import routes