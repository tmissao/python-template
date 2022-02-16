# pylint: disable=redefined-outer-name
import pytest
from .. import app
from ..common.fibonacci import Fibonacci


@pytest.mark.app
def test_run(mocker):
    mock_get_fibonacci = mocker.patch('demo.app.Fibonacci.get_fibonacci',
                                      return_value=21)
    mock_get_random_fibonacci = mocker.patch(
        'demo.app.Fibonacci.get_random_fibonacci')
    mock_get_multiple_random_fibonacci = mocker.patch(
        'demo.app.Fibonacci.get_multiple_random_fibonacci')

    assert app.run() == 21

    mock_get_fibonacci.assert_called_once()
    mock_get_fibonacci.assert_called_with(8)
    mock_get_random_fibonacci.assert_called_once()
    mock_get_random_fibonacci.assert_called_with()
    mock_get_multiple_random_fibonacci.assert_called_once()
    mock_get_multiple_random_fibonacci.assert_called_with()


@pytest.mark.app
def test_run_another_way(mocker):
    mock = mocker.patch('demo.app.Fibonacci')
    mock().get_fibonacci.return_value = 21

    assert app.run() == 21

    mock().get_fibonacci.assert_called_once()
    mock().get_fibonacci.assert_called_with(8)
    mock().get_random_fibonacci.assert_called_once()
    mock().get_random_fibonacci.assert_called_with()
    mock().get_multiple_random_fibonacci.assert_called_once()
    mock().get_multiple_random_fibonacci.assert_called_with()


@pytest.mark.app
def test_run_yet_another_way(mocker):
    mock_getfibonacci = mocker.patch.object(Fibonacci, 'get_fibonacci',
                                            return_value=21)
    mock_get_random_fibonacci = mocker.patch.object(Fibonacci,
                                                    'get_random_fibonacci')
    mock_get_multiple_random_fibonacci = mocker.patch.object(
        Fibonacci, 'get_multiple_random_fibonacci'
    )

    assert app.run() == 21

    mock_getfibonacci.assert_called_once()
    mock_getfibonacci.assert_called_with(8)
    mock_get_random_fibonacci.assert_called_once()
    mock_get_random_fibonacci.assert_called_with()
    mock_get_multiple_random_fibonacci.assert_called_once()
    mock_get_multiple_random_fibonacci.assert_called_with()