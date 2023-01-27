from qwe.reader import read_from_file


def create_test_data(test_data):
    with open("test/test_reader/test_qwe1", "a") as f_o:
        f_o.writelines(test_data)


def test_read_from_file():
    test_data = ['q\n', "w\n", "e\n"]
    create_test_data(test_data)
    assert test_data == read_from_file("qwe/qwe1")

