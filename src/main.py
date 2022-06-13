import json
import os

from sql_source.sql_operation import SqlInsert, JsonOperation


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
    #SqlInsert.insert_users(1, 'test1', 'test@example.com')
    #SqlInsert.insert_users(2, 'test2', 'test2@sample.com')
    #SqlInsert.insert_users(3, 'test3', 'test3@sample.com')

    # Test of data insertion into [autousers] table
    SqlInsert.insert_autousers(test1)
    SqlInsert.insert_autousers(test2)
    SqlInsert.insert_autousers(test3)
    SqlInsert.insert_autousers(test4)

    # Test using [autousers_ba] table back apostrophe
    SqlInsert.insert_autousers_ba(test1)
    SqlInsert.insert_autousers_ba(test2)
    SqlInsert.insert_autousers_ba(test3)
    SqlInsert.insert_autousers_ba(test4)

    # Test of data insertion into [json_tables] table
    SqlInsert.insert_json_tables("test_data", test_json_data)

    # Save data created within python in json format
    json_output(test_json_data)

    #Save data in DB in json format
    json_save_dir_path = os.path.join(parent_path(__file__, 1), 'resources/jsons/')
    JsonOperation.create_json(json_save_dir_path)



def json_output(data):
    with open(os.path.join(parent_path(__file__, 1), 'resources/jsons/python_json_sample.json'), 'w') as f:
        json.dump(data, f, indent=4)


def parent_path(path=__file__, f=0):
    return str('/'.join(os.path.abspath(path).split('/')[0:-1-f]))


def type_check(test: str):
    print("Data", end=" : ")
    print(test)
    print("Type", end=" : ")
    print(type(test))
    print("------------")


if __name__ == "__main__":
    main()
