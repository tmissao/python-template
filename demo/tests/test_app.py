# pylint: disable=redefined-outer-name
import pytest
from .. import app


@pytest.mark.app
def test_run(mocker):
    mock_get_fibonacci = mocker.patch('demo.app.Fibonacci.get_fibonacci',
                                      return_value=21)
    mock_get_random_fibonacci = mocker.patch(
        'demo.app.Fibonacci.get_random_fibonacci')
    mock_get_multiple_random_fibonacci = mocker.patch(
        'demo.app.Fibonacci.get_multiple_random_fibonacci')

    app.run()

    mock_get_fibonacci.assert_called_once()
    mock_get_fibonacci.assert_called_with(8)
    mock_get_random_fibonacci.assert_called_once()
    mock_get_random_fibonacci.assert_called_with()
    mock_get_multiple_random_fibonacci.assert_called_once()
    mock_get_multiple_random_fibonacci.assert_called_with()


@pytest.mark.app
def test_run_another_way(mocker):
    mock = mocker.patch('demo.app.Fibonacci')
    mock().get_fibonacci.return_value = 8
    mock().mock_get_random_fibonacci()
    mock().mock_get_multiple_random_fibonacci()

    app.run()

    mock().get_fibonacci.assert_called_once()
    mock().get_fibonacci.assert_called_with(8)
    mock().mock_get_random_fibonacci.assert_called_once()
    mock().mock_get_random_fibonacci.assert_called_with()
    mock().mock_get_multiple_random_fibonacci.assert_called_once()
    mock().mock_get_multiple_random_fibonacci.assert_called_with()
