from tinydb import TinyDB, Query, operations

main_db = TinyDB('main_db.json')
event_table = main_db.table("event_table")
keyword_table = main_db.table("keyword_table")
q = Query()

word_lists = [];
for keyword in keyword_table.all():
    word_list = [];
    word_list.append(keyword["keyword"])
    word_list += keyword["checkword"].split(",")
    word_lists.append(word_list)

for word_list in word_lists:
    for checkword in word_list[1:]:
        event_table.update(operations.add("keyword",word_list[0]+","), q.title.search(r"%s"% checkword))
        event_table.update(operations.add("keyword",word_list[0]+","), q.description.search(r"%s"% checkword))
