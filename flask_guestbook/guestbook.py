import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guestbook.sqlite3'
app.debug = True

db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement='auto')
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())


@app.route("/")
def index():
    messages = Message.query.all()[:10]
    context = {
        'title': 'Good guestbook!',
        'messages': messages,
    }
    return render_template('index.html', **context)
