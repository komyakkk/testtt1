import pytest


@pytest.fixture(autouse=True)
def clean_text_file():
    with open("test_qwe1", "w"):
        pass



