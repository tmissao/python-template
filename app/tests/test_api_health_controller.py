# pylint: disable=redefined-outer-name
import pytest
from freezegun import freeze_time
from ..api.health.controller import HealthAPI


@pytest.fixture
def instance():
    return HealthAPI()


@pytest.mark.health
def test_get_prefix(instance):
    expected = f'/{instance.NAMESPACE}'
    assert instance.get_prefix() == expected


@pytest.mark.health
def test_get_blueprint(instance):
    expected = instance.BLUEPRINT
    assert instance.get_blueprint() == expected


@pytest.mark.health
def test_get_register_blueprint(instance):
    expected = (instance.BLUEPRINT, f'/{instance.NAMESPACE}')
    assert instance.get_register_blueprint() == expected


@pytest.mark.health
@freeze_time("2012-01-14 03:21:34")
def test_health(client, instance):
    response = client.get(f'{instance.get_prefix()}/')
    res = response.get_json()
    assert response.status_code == 200
    assert res['running'] is True
    assert res['version'] == '0.0.1'
    assert res['date'] == '2012-01-14T03:21:34'
