from tinydb import TinyDB

event_db = TinyDB('event_db01.json')
keywords_db = TinyDB('keywords.json')
event_all = event_db.all()
keywords_all = keywords_db.all()

for keywords in keywords_db:
    print(keywords)

    # for event in event_all:
    #     print(event)
