import mysql.connector

def main():
    cnx = None

    try:
        cnx = mysql.connector.connect(
            user="koukemo",
            password="koukemo",
            host="127.0.0.1",
            database="koukemo"
        )

        cursor = cnx.cursor()

        sql = ('''
        INSERT INTO users
                (id, name, email)
            VALUES 
                (%s, %s, %s)
        ''')

        data = [
            ('1', 'test1', 'test@sample.com'),
            ('2', 'test2', 'test2@sample.com'),
            ('3', 'test3', 'test3@sample.com')
        ]

        cursor.executemany(sql, data)
        cnx.commit()

        print(f"{cursor.rowcount} records inserted.")

        cursor.close()

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()


if __name__ == "__main__":
    main()