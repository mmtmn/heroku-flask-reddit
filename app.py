from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://bc411967f1a7cb:349711ee@us-cdbr-iron-east-05.cleardb.net/heroku_9be86e38dfddff6'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable = False, unique = True)
    email = db.Column(db.String(120), nullable = False, unique = True)
    password = db.Column(db.String(120), nullable = False, unique=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/")
def index():
    return "Hello World!"



if __name__ == "__main__":
    app.run(debug=True)
    