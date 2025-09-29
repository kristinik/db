import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "mysql+pymysql://root:1111@127.0.0.1:3306/your_database1234")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")
