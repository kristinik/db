# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from app.config import Config
# import mysql.connector
# from mysql.connector import errorcode
# import os
#
#
# db = SQLAlchemy()
#
# def create_app():
#
#     app = Flask(__name__)
#     app.config.from_object(Config)
#
#     # Ініціалізуємо SQLAlchemy після створення додатку
#     db.init_app(app)
#
#     # Створюємо базу даних, якщо вона не існує
#     create_database()
#
#     with app.app_context():
#         # Імпортуємо моделі
#         from app.domain.brand import Brand
#         from app.domain.menu import Menu
#         from app.domain.vendingmachine import VendingMachine
#         from app.domain.technician import Technician
#         from app.domain.product import Product
#
#         # Скидаємо і створюємо таблиці
#         db.drop_all()  # Це видалить всі таблиці
#         db.create_all()  # Створюємо нові таблиці
#
#         populate_data()  # Викликаємо функцію заповнення даних
#
#     # Інші ініціалізації
#     return app
#
# def create_database():
#     try:
#         connection = mysql.connector.connect(
#             host='127.0.0.1',
#             user='root',
#             password='1111',
#         )
#         cursor = connection.cursor()
#         cursor.execute("CREATE DATABASE IF NOT EXISTS your_database123")  # Змініть на вашу фактичну назву
#         cursor.close()
#         connection.close()
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print("Something is wrong with your user name or password")
#         elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             print("Database does not exist")
#         else:
#             print(err)
#
# def populate_data():
#     sql_file_path = os.path.abspath('data.sql')
#     if os.path.exists(sql_file_path):
#         try:
#             connection = mysql.connector.connect(
#                 host='127.0.0.1',
#                 user='root',
#                 password='1111',
#                 database='your_database123'  # Вказати правильну назву бази даних
#             )
#             cursor = connection.cursor()
#             with open(sql_file_path, 'r') as sql_file:
#                 sql_text = sql_file.read()
#                 sql_statements = sql_text.split(';')
#                 for statement in sql_statements:
#                     statement = statement.strip()
#                     if statement:
#                         try:
#                             cursor.execute(statement)
#                             connection.commit()
#                         except mysql.connector.Error as error:
#                             print(f"Error executing SQL statement: {error}")
#                             connection.rollback()
#         finally:
#             cursor.close()
#             connection.close()
#     else:
#         print("SQL file does not exist")

import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.root import register_routes
import os
import sys

print(sys.path)
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    register_routes(app)
    create_database()
    create_tables(app)
    populate_data()
    return app


def create_database():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='1111',
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS your_database1234")
    cursor.close()
    connection.close()


def create_tables(app):
    with app.app_context():
        db.create_all()


def populate_data():
    sql_file_path = os.path.abspath('data.sql')
    if os.path.exists('data.sql'):
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='1111',
            database='your_database1234'
        )
        cursor = connection.cursor()
        with open(sql_file_path, 'r') as sql_file:
            sql_text = sql_file.read()
            sql_statements = sql_text.split(';')
            for statement in sql_statements:

                statement = statement.strip()
                if statement:
                    try:
                        cursor.execute(statement)
                        connection.commit()
                    except mysql.connector.Error as error:
                        print(f"Error executing SQL statement: {error}")
                        connection.rollback()
        cursor.close()
        connection.close()
