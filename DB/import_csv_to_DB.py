import csv
import os
import json
import pandas as pd
from pymongo import MongoClient

def mongoimport(csv_path, col_name):
    HOST = 'cluster0.vxhjvg6.mongodb.net'
    USER = 'alwjd7858'
    PASSWORD = 'fwjlfYBQvE2rRJsR'
    DATABASE_NAME = 'recommendations'

    MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"
    client = MongoClient(MONGO_URI)
    
    # 데이터베이스 접근
    db = client[DATABASE_NAME]
    
    # 콜렉션 접근
    col = db[col_name]
    
    data = pd.read_csv(csv_path, low_memory=False)
    payload = json.loads(data.to_json(orient='records'))
    
    for data in payload:
        try:
            col.insert_one(data)
        except Exception as e:
            print("Error")

    return None

# mongoimport(os.path.join(os.getcwd(), 'ratings_books.csv'), 'Ratings')