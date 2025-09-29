import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "mysql+pymysql://appuser:IlhMKrDeEroXDRrXFMNV@"
        "appdb.cr6squ8gqocf.eu-central-1.rds.amazonaws.com:3306/your_database1234"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
