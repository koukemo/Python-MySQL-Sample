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


class Sqlshow:
    @staticmethod
    def show_all_tables():
        ctx = mysql.connector.connect(**config)
        cursor = ctx.cursor()

        cursor.execute("SHOW TABLES")

        for table in cursor:
            print(table[0])
        cursor.close()


class Sqlgetdata:
    @staticmethod
    def get_all_tables():
        ctx = mysql.connector.connect(**config)
        cursor = ctx.cursor()

        cursor.execute("SHOW TABLES")

        all_tables = ()
        for table in cursor:
            all_tables = all_tables + table
        cursor.close()
        return all_tables


class Sqldelete:
    @staticmethod
    def delete_all_table():
        ctx = mysql.connector.connect(**config)
        cursor = ctx.cursor()

        tables = Sqlgetdata.get_all_tables()

        for table in tables:
            if table == "schema_migrations":
                continue
            sql = "TRUNCATE TABLE {};"
            cursor.execute(sql.format(table))
            ctx.commit()
        print("All data in the created table has been deleted!")
        cursor.close()
