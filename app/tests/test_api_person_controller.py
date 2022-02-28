# pylint: disable=redefined-outer-name
import pytest
from ..api.people.controller import PersonAPI
from ..api.people.domain import PersonDomain
from ..api.people.model import Person


@pytest.fixture
def instance():
    return PersonAPI()


@pytest.fixture
def person():
    return Person(id=1, first_name='Tiago', last_name='Missão',
                  age=28, gender='M', occupation='Software Engineer')


@pytest.fixture
def person_json():
    return {
        'id': 1, 'firstName': 'Tiago', 'lastName': 'Missão',
        'age': 28, 'gender': 'M', 'occupation': 'Software Engineer'
    }


@pytest.mark.people
def test_get_prefix(instance):
    expected = f'/{instance.NAMESPACE}'
    assert instance.get_prefix() == expected


@pytest.mark.people
def test_get_blueprint(instance):
    expected = instance.BLUEPRINT
    assert instance.get_blueprint() == expected


@pytest.mark.people
def test_get_register_blueprint(instance):
    expected = (instance.BLUEPRINT, f'/{instance.NAMESPACE}')
    assert instance.get_register_blueprint() == expected


@pytest.mark.people
def test_get_person(mocker, client, instance, person, person_json):
    person_id = person.id
    mock_domain_get = mocker.patch.object(PersonDomain,
                                          'get', return_value=person)
    response = client.get(f'{instance.get_prefix()}/{person_id}')
    res = response.get_json()

    assert response.status_code == 200
    assert res == person_json
    mock_domain_get.assert_called_with(person_id)
    mock_domain_get.assert_called_once()


@pytest.mark.people
def test_get_person_error(mocker, client, instance, person):
    person_id = person.id
    mock_domain_get = mocker.patch.object(PersonDomain,
                                          'get', side_effect=ValueError())
    response = client.get(f'{instance.get_prefix()}/{person_id}')

    assert response.status_code == 404
    mock_domain_get.assert_called_with(person_id)
    mock_domain_get.assert_called_once()


@pytest.mark.people
def test_get_people(mocker, client, instance, person, person_json):
    mock_domain_get_all = mocker.patch.object(PersonDomain,
                                              'get_all', return_value=[person])
    response = client.get(f'{instance.get_prefix()}/list')
    res = response.get_json()

    assert response.status_code == 200
    assert res == [person_json]
    mock_domain_get_all.assert_called_with()
    mock_domain_get_all.assert_called_once()


@pytest.mark.people
def test_put(mocker, client, instance, person, person_json):
    person_id = person.id
    mock_domain_replace = mocker.patch.object(PersonDomain,
                                              'replace', return_value=person)
    response = client.put(f'{instance.get_prefix()}/{person_id}',
                          json=person_json)
    res = response.get_json()

    assert response.status_code == 200
    assert res == person_json
    mock_domain_replace.assert_called_with(person)
    mock_domain_replace.assert_called_once()


@pytest.mark.people
def test_put_error(mocker, client, instance, person, person_json):
    person_id = person.id
    mock_domain_replace = mocker.patch.object(PersonDomain,
                                              'replace',
                                              side_effect=ValueError())
    response = client.put(f'{instance.get_prefix()}/{person_id}',
                          json=person_json)

    assert response.status_code == 404
    mock_domain_replace.assert_called_with(person)
    mock_domain_replace.assert_called_once()


@pytest.mark.people
def test_post(mocker, client, instance, person, person_json):
    mock_domain_add = mocker.patch.object(PersonDomain, 'add',
                                          return_value=person)
    response = client.post(f'{instance.get_prefix()}/',
                           json=person_json)
    res = response.get_json()

    assert response.status_code == 201
    assert res == person_json
    mock_domain_add.assert_called_with(person)
    mock_domain_add.assert_called_once()


@pytest.mark.people
def test_post_error(mocker, client, instance, person, person_json):
    mock_domain_add = mocker.patch.object(PersonDomain, 'add',
                                          side_effect=ValueError())
    response = client.post(f'{instance.get_prefix()}/',
                           json=person_json)

    assert response.status_code == 404
    mock_domain_add.assert_called_with(person)
    mock_domain_add.assert_called_once()


@pytest.mark.people
def test_patch(mocker, client, instance, person):
    person_id = person.id
    patch_json = {'firstName': 'Fran', 'gender': 'F', 'occupation': 'Cashier'}
    mock_domain_update = mocker.patch.object(PersonDomain, 'update',
                                             side_effect=ValueError())
    response = client.patch(f'{instance.get_prefix()}/{person_id}',
                            json=patch_json)

    assert response.status_code == 404
    mock_domain_update.assert_called_with(person_id, first_name='Fran',
                                          gender='F', occupation='Cashier')
    mock_domain_update.assert_called_once()


@pytest.mark.people
def test_patch_error(mocker, client, instance, person):
    person_id = person.id
    patch_json = {'firstName': 'Fran', 'gender': 'F', 'occupation': 'Cashier'}
    patched_person = Person(id=1, first_name='Fran', last_name='Missão',
                            age=28, gender='F', occupation='Cashier')
    expected_json = {
        'id': 1, 'firstName': 'Fran', 'lastName': 'Missão', 'age': 28,
        'gender': 'F', 'occupation': 'Cashier'
    }
    mock_domain_update = mocker.patch.object(PersonDomain, 'update',
                                             return_value=patched_person)
    response = client.patch(f'{instance.get_prefix()}/{person_id}',
                            json=patch_json)

    res = response.get_json()

    assert response.status_code == 200
    assert res == expected_json
    mock_domain_update.assert_called_with(person_id, first_name='Fran',
                                          gender='F', occupation='Cashier')
    mock_domain_update.assert_called_once()


@pytest.mark.people
def test_delete(mocker, client, instance, person):
    person_id = person.id
    mock_domain_delete = mocker.patch.object(PersonDomain, 'delete')
    response = client.delete(f'{instance.get_prefix()}/{person_id}')

    assert response.status_code == 204
    mock_domain_delete.assert_called_with(person_id)
    mock_domain_delete.assert_called_once()


@pytest.mark.people
def test_delete_error(mocker, client, instance, person):
    person_id = person.id
    mock_domain_delete = mocker.patch.object(PersonDomain, 'delete',
                                             side_effect=ValueError())
    response = client.delete(f'{instance.get_prefix()}/{person_id}')

    assert response.status_code == 404
    mock_domain_delete.assert_called_with(person_id)
    mock_domain_delete.assert_called_once()
