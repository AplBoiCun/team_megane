#import get_timelines
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from tinydb import TinyDB, Query
db = TinyDB('user_db.json')
db.purge()


@app.route("/")
#@app.route("/index")
def index():

  return render_template('index.html')


@app.route("/result")
def add():
  db.insert({

      "area": request.args.get("area"),
      'ID': request.args.get('twitter')

  })
  #get_timelines.get(request.args.get('twitter'))

  return render_template('result.html', posts=db.all())

#@app.route("/reset")
# def reset():
#    if db is not None:
#        db.purge()
#    db.insert({'adress': 'Pecha','area':'Welcome','ID':'id'})
#    return index()


if __name__ == "__main__":
  app.run(debug=True, port=5000, host="0.0.0.0")
