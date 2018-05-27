from tinydb import TinyDB, Query, operations

def select(id):
    events = []
    q = Query()
    main_db = TinyDB('main_db.json')
    event_table = main_db.table("event_table")
    user_table = main_db.table("user_table")
    user_keywords = user_table.search(q.ID.matches(id))[0]['keyword'][:-1].split(",")
    for keyword in user_keywords:
        events += event_table.search(q.keyword.search(r"%s"% keyword))    
    return(events)
