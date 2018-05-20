# -*- coding: utf-8 -*-
import os
from os.path import join, dirname
from dotenv import load_dotenv
import json
from requests_oauthlib import OAuth1Session  # OAuthのライブラリの読み込み
from tinydb import TinyDB, Query
db = TinyDB('tweet_db.json')

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


CK = os.environ.get("CONSUMER_KEY")
CS = os.environ.get("CONSUMER_SECRET")
AT = os.environ.get("ACCESS_TOKEN")
ATS = os.environ.get("ACCESS_TOKEN_SECRET")
twitter = OAuth1Session(CK, CS, AT, ATS)  # 認証処理

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"  # タイムライン取得エンドポイント

params = {'count': 3}  # 取得数
res = twitter.get(url, params=params)

if res.status_code == 200:  # 正常通信出来た場合
  timelines = json.loads(res.text)  # レスポンスからタイムラインリストを取得
  for line in timelines:  # タイムラインリストをループ処理
    db.insert({
        'text': line['text']
    })
else:  # 正常通信出来なかった場合
  print("Failed: %d" % res.status_code)
