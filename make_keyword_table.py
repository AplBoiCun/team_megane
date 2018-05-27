from tinydb import TinyDB, Query, operations
main_db = TinyDB('main_db.json')
keyword_table = main_db.table("keyword_table")
keyword_table.purge()

keywords_list = [
{"keyword": "祭り","checkword": "まつり,フェス,フェスティバル,音楽,花火"},
{"keyword": "グルメ","checkword": "美味しい,ごはん,ラーメン,二郎,旨い,スイーツ,和食,洋食,中華"},
{"keyword": "アニメ・ゲーム","checkword": "今期,覇権,最新話,はいいぞ,は良いぞ,課金,好きなアニメあったらRT,ガチャ,アニメ好きと繋がりたい,缶バッジ,アニメイト,絵師,ゲーム,アニメ"},
{"keyword": "Web","checkword": "web,Web,WEB,フロントエンド,バッグエンド,Rails,Django,Dlask,HTML,CSS,Javascript"},
{"keyword": "データサイエンス","checkword": "データ,R,Python,機械学習,人工知能"},
{"keyword": "仮想通貨", "checkword": "ブロックチェーン,Bitcoin,仮想通貨,マイニング"},
{"keyword": "量子コンピュータ", "checkword": "量子コンピュータ"}

]

keyword_table.insert_multiple(keywords_list)
