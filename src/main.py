from sql_source.sql_operation import Sqlinsert


def main():
    # test datas
    test1 = "test"
    test2 = "test2_test"
    test3 = ("test3")
    test4 = "(test4)"

    type_check(test1)
    type_check(test2)
    type_check(test3)
    type_check(test4)

    test_json_data = [
        {
            'name': 'Test',
            'number': 0,
            'frame': 0
        },
        {
            'name': 'Test2',
            'number': 1,
            'frame': 10
        },
        {
            'name': 'Test3',
            'number': 2,
            'frame': 20
        }
    ]

    type_check(test_json_data)

    # Test of data insertion into [users] table
    Sqlinsert.insert_users(1, 'test1', 'test@example.com')
    Sqlinsert.insert_users(2, 'test2', 'test2@sample.com')
    Sqlinsert.insert_users(3, 'test3', 'test3@sample.com')

    # Test of data insertion into [autousers] table
    Sqlinsert.insert_autousers(test1)
    Sqlinsert.insert_autousers(test2)
    Sqlinsert.insert_autousers(test3)
    Sqlinsert.insert_autousers(test4)

    # Test using [autousers_ba] table back apostrophe
    Sqlinsert.insert_autousers_ba(test1)
    Sqlinsert.insert_autousers_ba(test2)
    Sqlinsert.insert_autousers_ba(test3)
    Sqlinsert.insert_autousers_ba(test4)

    # Test of data insertion into [json_tables] table
    Sqlinsert.insert_json_tables("test_data", test_json_data)


def type_check(test: str):
    print("Data", end=" : ")
    print(test)
    print("Type", end=" : ")
    print(type(test))
    print("------------")


if __name__ == "__main__":
    main()
