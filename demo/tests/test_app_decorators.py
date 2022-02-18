# pylint: disable=redefined-outer-name
import pytest
import mock
from .. import app
from ..commons.fibonacci import Fibonacci


@pytest.mark.app
@mock.patch('demo.app.Fibonacci.get_multiple_random_fibonacci')
@mock.patch('demo.app.Fibonacci.get_random_fibonacci')
@mock.patch('demo.app.Fibonacci.get_fibonacci', return_value=21)
def test_run(mock_get_fibonacci, mock_get_random_fibonacci,
             mock_get_multiple_random_fibonacci):

    assert app.run() == 21

    mock_get_fibonacci.assert_called_once()
    mock_get_fibonacci.assert_called_with(8)
    mock_get_random_fibonacci.assert_called_once()
    mock_get_random_fibonacci.assert_called_with()
    mock_get_multiple_random_fibonacci.assert_called_once()
    mock_get_multiple_random_fibonacci.assert_called_with()


@pytest.mark.app
@mock.patch('demo.app.Fibonacci')
def test_run_another_way(mock):
    mock().get_fibonacci.return_value = 21

    assert app.run() == 21

    mock().get_fibonacci.assert_called_once()
    mock().get_fibonacci.assert_called_with(8)
    mock().get_random_fibonacci.assert_called_once()
    mock().get_random_fibonacci.assert_called_with()
    mock().get_multiple_random_fibonacci.assert_called_once()
    mock().get_multiple_random_fibonacci.assert_called_with()


@pytest.mark.app
@mock.patch.object(Fibonacci, 'get_multiple_random_fibonacci')
@mock.patch.object(Fibonacci, 'get_random_fibonacci')
@mock.patch.object(Fibonacci, 'get_fibonacci',  return_value=21)
def test_run_yet_another_way(mock_getfibonacci, mock_get_random_fibonacci,
                             mock_get_multiple_random_fibonacci):

    assert app.run() == 21

    mock_getfibonacci.assert_called_once()
    mock_getfibonacci.assert_called_with(8)
    mock_get_random_fibonacci.assert_called_once()
    mock_get_random_fibonacci.assert_called_with()
    mock_get_multiple_random_fibonacci.assert_called_once()
    mock_get_multiple_random_fibonacci.assert_called_with()
