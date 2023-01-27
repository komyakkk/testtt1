from qwe.main import division
import pytest


# тест на корретность результата
@pytest.mark.parametrize("a, b, expected_result", [(15, 5, 3),
                                                   (123, 3, 41),
                                                   (-32, 8, -4)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result

# тест на ошибку при делении на ноль/str
@pytest.mark.parametrize("expected_exception, divider, division1", [(ZeroDivisionError, 0, 10),
                                                                    (TypeError, "546", 43)])
def test_division_with_error(expected_exception, divider, division1):
    with pytest.raises(expected_exception):
        division(division1, divider)
