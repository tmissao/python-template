# pylint: disable=redefined-outer-name
import pytest
from freezegun import freeze_time
from ..api.health.model import Health, HealthSchema


@pytest.fixture
@freeze_time("2012-01-14 03:21:34")
def instance():
    return Health()


@pytest.fixture
def health_schema():
    return HealthSchema()


@pytest.fixture
def health_schema_data():
    return {}


@pytest.mark.health
def test_health_instance_init(instance):
    assert instance.running is True
    assert instance.version == "0.0.1"
    assert str(instance.date) == "2012-01-14 03:21:34"


@pytest.mark.health
def test_health_instance_repr(instance):
    expected = (f'<Health(running={instance.running}, date={instance.date}, '
                f'version={instance.version})>')
    assert repr(instance) == expected


@pytest.mark.health
@freeze_time("2012-01-14 03:21:34")
def test_healthschema_to_health(health_schema, health_schema_data, instance):
    expected = (f'<Health(running={instance.running}, date={instance.date}, '
                f'version={instance.version})>')
    assert repr(health_schema.make_health(health_schema_data)) == expected
