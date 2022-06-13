import mysql.connector
import json
import os

from sql_source.config import config


class SqlGetdata:
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

    @staticmethod
    def get_json_data(table_name: str, column: str = "*"):
        ctx = mysql.connector.connect(**config)
        cursor = ctx.cursor()

        sql = "SELECT {} FROM {};"
        cursor.execute(sql.format(column, table_name))

        json_datas = {}
        for data in cursor:
            json_datas[data[0]] = json.loads(data[2])
        cursor.close()
        return json_datas


class SqlInsert:
    @staticmethod
    def insert_users(id: int, name: str, email: str):
        ctx = mysql.connector.connect(**config)
        cursor = ctx.cursor()

        cursor.execute("INSERT INTO users(id, name, email) VALUES (%s, %s, %s)",
                    (id, name, email))
        ctx.commit()
        ctx.close()

    @staticmethod
    def insert_autousers(name: str):
        ctx = mysql.connector.connect(**config)
        cursor = ctx.cursor()

        cursor.execute("INSERT INTO autousers(name) VALUES (%s)",
                    (name,))
        ctx.commit()
        ctx.close()

    @staticmethod
    def insert_autousers_ba(name: str):
        ctx = mysql.connector.connect(**config)
        cursor = ctx.cursor()

        cursor.execute("INSERT INTO autousers_ba(name) VALUES (%s)",
                    (name,))
        ctx.commit()
        ctx.close()

    @staticmethod
    def insert_json_tables(title: str, data):
        ctx = mysql.connector.connect(**config)
        cursor = ctx.cursor()

        json_data = json.dumps(data)

        cursor.execute("INSERT INTO json_tables(title, json_datas) VALUES (%s, %s)",
                    (title, json_data))
        ctx.commit()
        ctx.close()


class SqlShow:
    @staticmethod
    def show_all_tables():
        ctx = mysql.connector.connect(**config)
        cursor = ctx.cursor()

        cursor.execute("SHOW TABLES")

        for table in cursor:
            print(table[0])
        cursor.close()

    @staticmethod
    def show_table_data(table_name: str, column: str = "*"):
        ctx = mysql.connector.connect(**config)
        cursor = ctx.cursor()

        sql = "SELECT {} FROM {};"
        cursor.execute(sql.format(column, table_name))

        print("table :", table_name)
        for data in cursor:
            print(data)
        cursor.close()


class SqlDelete:
    @staticmethod
    def delete_all_table():
        ctx = mysql.connector.connect(**config)
        cursor = ctx.cursor()

        tables = SqlGetdata.get_all_tables()

        for table in tables:
            if table == "schema_migrations":
                continue
            sql = "TRUNCATE TABLE {};"
            cursor.execute(sql.format(table))
            ctx.commit()
        print("All data in the created table has been deleted!")
        cursor.close()


class JsonOperation:
    @staticmethod
    def create_json(save_dir_path: str):
        ctx = mysql.connector.connect(**config)
        cursor = ctx.cursor()

        json_data = SqlGetdata.get_json_data("json_tables")

        for key, value in json_data.items():
            save_file_name = "db_json_sample_" + str(key)
            with open(os.path.join(save_dir_path, save_file_name) + '.json', 'w') as f:
                json.dump(value, f, indent=4)
