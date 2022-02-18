# pylint: disable=redefined-outer-name
import pytest
from ..commons.fibonacci import Fibonacci


@pytest.fixture
def instance():
    return Fibonacci()


@pytest.fixture
def fibonacci_invalid_input():
    return -1


@pytest.mark.fibonacci
@pytest.mark.parametrize("num, expected", [
    (0, 0), (1, 1), (2, 1), (3, 2), (8, 21), (28, 317811)
])
def test_get_fibonacci(instance, num, expected):
    assert instance.get_fibonacci(num) == expected


@pytest.mark.fibonacci
def test_get_fibonacci_invalid_arg(instance, fibonacci_invalid_input):
    with pytest.raises(ValueError):
        instance.get_fibonacci(fibonacci_invalid_input)


@pytest.mark.fibonacci
def test_get_random_fibonacci(mocker, instance):
    mock = mocker.patch('random.randrange', return_value=8)
    assert instance.get_random_fibonacci() == (8, 21)
    mock.assert_called_once()
    mock.assert_called_with(1, 20)


@pytest.mark.fibonacci
def test_get_multiple_random_fibonacci(mocker, instance):
    mock = mocker.patch('random.randrange', side_effect=[3, 15, 7, 8])
    assert instance.get_multiple_random_fibonacci() == [
        (15, 610), (7, 13), (8, 21)
    ]
    assert mock.call_count == 4
    assert mock.call_args_list == [
        ((1, 5), ), ((1, 20), ), ((1, 20), ), ((1, 20), )
    ]
