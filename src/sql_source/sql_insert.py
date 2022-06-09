import mysql.connector

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
    