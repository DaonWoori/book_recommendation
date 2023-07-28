import pandas as pd
from pymongo import MongoClient

HOST = 'cluster0.vxhjvg6.mongodb.net'
USER = 'alwjd7858'
PASSWORD = 'fwjlfYBQvE2rRJsR'
DATABASE_NAME = 'recommendations'

# MONGO_URI = f"mongodb://alwjd7858:{PASSWORD}@ac-w6utfpd-shard-00-00.vxhjvg6.mongodb.net:27017,ac-w6utfpd-shard-00-01.vxhjvg6.mongodb.net:27017,ac-w6utfpd-shard-00-02.vxhjvg6.mongodb.net:27017/?ssl=true&replicaSet=atlas-8wigrn-shard-0&authSource=admin&retryWrites=true&w=majority"
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)

# 데이터베이스 접근
db = client[DATABASE_NAME]

def get_ratings(book_title):
    # 콜렉션 접근
    col = db.Ratings
    # 책 제목으로 데이터 찾기
    return col.find_one({'Book-Title':book_title}, {'_id':False})
