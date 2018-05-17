from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from tinydb import TinyDB, Query
db = TinyDB('chat_db.json')

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', posts = db.all())

@app.route("/add")
def add():
    db.insert({
        'user': request.args.get('user'),
        'message': request.args.get('message')
    })
    return index()

@app.route("/reset")
def reset():
    if db is not None:
        db.purge()
    db.insert({'user': 'Pecha','message':'Welcome :)'})
    return index()

if __name__ == "__main__":
    app.run(debug = True, port=5000, host="0.0.0.0")
