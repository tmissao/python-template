# pylint: disable=redefined-outer-name
import pytest
from ..api.people.domain import PersonDomain
from ..api.people.model import Person


@pytest.fixture
def domain():
    return PersonDomain()


@pytest.fixture
def person():
    return Person(id=1, first_name='Tiago', last_name='Missão',
                  age=28, gender='M', occupation='Software Engineer')


@pytest.fixture
def person2():
    return Person(id=None, first_name='Fran', last_name='Missão',
                  age=28, gender='F', occupation=None)


@pytest.mark.people
def test_add_with_id(domain, person):
    result = domain.add(person)
    assert result == person


@pytest.mark.people
def test_add_same_id(domain, person):
    with pytest.raises(ValueError):
        domain.add(person)
        domain.add(person)


@pytest.mark.people
def test_add_without_id(mocker, domain, person2):
    randint = 8
    mocker.patch('random.randint', return_value=randint)
    res = domain.add(person2)
    assert person2 == res
    assert person2.id == randint


@pytest.mark.people
def test_add_without_id_collision(mocker, domain, person, person2):
    randint = [1, 1, 5]
    mock_randint = mocker.patch('random.randint', side_effect=randint)
    domain.add(person)
    res = domain.add(person2)
    assert person2 == res
    assert person2.id == randint[-1]
    assert mock_randint.call_count == 3


@pytest.mark.people
def test_get_empty(domain):
    with pytest.raises(ValueError):
        domain.get(-1)


@pytest.mark.people
def test_get(domain, person, person2):
    domain.add(person)
    domain.add(person2)

    res = domain.get(person.id)
    res2 = domain.get(person2.id)

    assert res == person
    assert res2 == person2


@pytest.mark.people
def test_get_all_empty(domain):
    res = domain.get_all()
    assert not list(res)


@pytest.mark.people
def test_get_all(domain, person, person2):
    domain.add(person)
    domain.add(person2)

    res = domain.get_all()

    assert person in res
    assert person2 in res


@pytest.mark.people
def test_replace(domain, person, person2):
    domain.add(person)
    person2.id = person.id
    domain.replace(person2)

    res = domain.get(person.id)

    assert res == person2


@pytest.mark.people
def test_replace_error(domain, person2):
    with pytest.raises(ValueError):
        domain.replace(person2)


@pytest.mark.people
def test_update(domain, person):
    domain.add(person)
    patch = {'first_name': 'John', 'occupation': 'Student'}
    res = domain.update(person.id, **patch)
    assert res.id == person.id
    assert res.first_name == patch['first_name']
    assert res.last_name == person.last_name
    assert res.age == person.age
    assert res.gender == person.gender
    assert res.occupation == patch['occupation']


@pytest.mark.people
def test_update_error(domain, person):
    with pytest.raises(ValueError):
        domain.add(person)
        patch = {'first_name': 'John', 'occupation': 'Student'}
        domain.update(-1, **patch)


@pytest.mark.people
def test_delete(domain, person):
    domain.add(person)
    assert domain.delete(person.id)


@pytest.mark.people
def test_delete_error(domain):
    with pytest.raises(ValueError):
        domain.delete(-1)
