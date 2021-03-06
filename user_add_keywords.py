from tinydb import TinyDB, Query, operations

def add(id):
    main_db = TinyDB('main_db.json')
    keyword_table = main_db.table("keyword_table")
    timeline_table = main_db.table("timeline_table")
    user_table = main_db.table("user_table")
    q = Query()

    word_lists = [];
    for keyword in keyword_table.all():
        word_list = [];
        word_list.append(keyword["keyword"])
        word_list += keyword["checkword"].split(",")
        word_lists.append(word_list)

    for word_list in word_lists:
        checker = 0
        for checkword in word_list[1:]:
            checker += len(timeline_table.search(q.text.search(r"%s"% checkword)))
        if checker > 0:
            user_table.update(operations.add("keyword",word_list[0]+","), q.ID.matches(r"%s"% id))
