import os
from sqlalchemy import text
from app import create_app, db

app = create_app()

def run_sql_file(path: str):
    if not os.path.exists(path):
        print(f"{path} not found, skipping.")
        return
    with app.app_context():
        engine = db.engine
        with engine.connect() as conn:
            with open(path, "r", encoding="utf-8") as f:
                sql_all = f.read()
            for stmt in [s.strip() for s in sql_all.split(";") if s.strip()]:
                conn.exec_driver_sql(stmt)
    print("data.sql applied")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    run_sql_file("data.sql")
