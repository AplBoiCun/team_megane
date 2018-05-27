from tinydb import TinyDB, Query, operations
main_db = TinyDB('main_db.json')
keyword_table = main_db.table("keyword_table")
keyword_table.purge()

keywords_list = [
{"keyword": "祭り","checkword": "まつり,フェス,フェスティバル,音楽,花火"},
{"keyword": "グルメ","checkword": "美味しい,ごはん,ラーメン,二郎,旨い"},
{"keyword": "アニメ・ゲーム","checkword": "今期,覇権,最新話,はいいぞ,は良いぞ,課金,好きなアニメあったらRT,ガチャ,アニメ好きと繋がりたい,缶バッジ,アニメイト,絵師,ゲーム,アニメ"},
]

keyword_table.insert_multiple(keywords_list)
