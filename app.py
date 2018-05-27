from flask import Flask, render_template, request, redirect, url_for
from time import sleep
import get_timelines
import user_add_keywords
import event_select
import sort_by_distance


app = Flask(__name__)

from tinydb import TinyDB, Query

db = TinyDB('main_db.json')                  # データベース作成
user_table = db.table('user_table')
timeline_table = db.table('timeline_table')
user_table.purge()
q=Query()


@app.route("/")
#@app.route("/index")
def index():

  return render_template('index.html')


@app.route("/result")
def add():
  area = request.args.get('area')
  id = request.args.get('twitter')
  user_table.insert({

      'area': area,
      'ID': id,
      'keyword': ''

  })
  get_timelines.get(id)
  print("timelineの長さは"+str(len(timeline_table)))
  user_add_keywords.add(id)
  events = event_select.select(id)
  events = sort_by_distance.get(events, area)
  user = user_table.search(q.ID.matches(id))
  user_keyword = '、'.join(list(set(user[0]["keyword"][:-1].split(","))))



  return render_template('result.html', posts=events, user_id=id, user_keyword=user_keyword)

#@app.route("/reset")
# def reset():
#    if db is not None:
#        db.purge()
#    db.insert({'adress': 'Pecha','area':'Welcome','ID':'id'})
#    return index()


if __name__ == "__main__":
  app.run(debug=True, port=5000, host="0.0.0.0")
