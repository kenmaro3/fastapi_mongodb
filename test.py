#インポート
import pymongo
import sys

MONGODB_URL='mongodb://localhost:27017/'
#クライアントの作成とDocumentDBとの接続
client = pymongo.MongoClient(MONGODB_URL)


#データベースの指定
db = client.customer_db
#コレクションの指定
col = db.customer

#ドキュメントの挿入
#db.col.insert_one({"ID":"1", "Name":"test taro" })
#db.col.insert_one({"ID":"2", "Name":"test jiro" })
#db.col.insert_one({"ID":"3", "Name":"test saburo" })

#コレクション内の全ドキュメントの検索
result = db.col.find()

for el in result:
    print(el)

#接続の終了
client.close()