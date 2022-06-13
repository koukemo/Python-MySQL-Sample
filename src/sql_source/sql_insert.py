import mysql.connector
import json

from sql_source.config import config

class Sqlinsert:
    @staticmethod
    def insert_users(id: int, name: str, email: str):
        ctx = mysql.connector.connect(**config)
        cur = ctx.cursor()

        cur.execute("INSERT INTO users(id, name, email) VALUES (%s, %s, %s)",
                    (id, name, email))
        ctx.commit()
        ctx.close()

    @staticmethod
    def insert_autousers(name: str):
        ctx = mysql.connector.connect(**config)
        cur = ctx.cursor()

        cur.execute("INSERT INTO autousers(name) VALUES (%s)",
                    (name,))
        ctx.commit()
        ctx.close()

    @staticmethod
    def insert_autousers_ba(name: str):
        ctx = mysql.connector.connect(**config)
        cur = ctx.cursor()

        cur.execute("INSERT INTO autousers_ba(name) VALUES (%s)",
                    (name,))
        ctx.commit()
        ctx.close()

    @staticmethod
    def insert_json_tables(title: str, data):
        ctx = mysql.connector.connect(**config)
        cur = ctx.cursor()

        json_data = json.dumps(data)

        cur.execute("INSERT INTO json_tables(title, json_datas) VALUES (%s, %s)",
                    (title, json_data))
        ctx.commit()
        ctx.close()
    