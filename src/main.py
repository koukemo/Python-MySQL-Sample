from sql_source.sql_insert import Sqlinsert

def main():
    Sqlinsert.insert_users(1, 'test1', 'test@example.com')
    Sqlinsert.insert_users(2, 'test2', 'test2@sample.com')
    Sqlinsert.insert_users(3, 'test3', 'test3@sample.com')

    test1 = "test"
    test2 = "test2_test"
    test3 = ("test3")
    test4 = "(test4)"

    type_check(test1)
    type_check(test2)
    type_check(test3)
    type_check(test4)
    
    Sqlinsert.insert_autousers(test1)
    Sqlinsert.insert_autousers(test2)
    Sqlinsert.insert_autousers(test3)
    Sqlinsert.insert_autousers(test4)

def type_check(test: str):
    print("Data", end=" : ")
    print(test)
    print("Type", end=" : ")
    print(type(test))
    print("------------")

if __name__ == "__main__":
    main()