
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# dotenv 라이브러리 import
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# 환경 변수 사용
mongodb_id = os.getenv("mongodb-id")
mongodb_pw = os.getenv("mongodb-pw")


uri = f"mongodb+srv://{mongodb_id}:{mongodb_pw}@devdoe.7ca7a.mongodb.net/?retryWrites=true&w=majority&appName=devdoe"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)