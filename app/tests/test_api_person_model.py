# pylint: disable=redefined-outer-name
import pytest
from ..api.people.model import Gender, Person, PersonSchema


@pytest.fixture
def person():
    return Person(id=1, first_name='Tiago', last_name='Missão',
                  age=28, gender='M', occupation='Software Engineer')


@pytest.fixture
def person_schema():
    return PersonSchema()


@pytest.fixture
def person_schema_data():
    return {'id': 1, 'first_name': 'Tiago', 'last_name': 'Missão',
            'age': 28, 'gender': 'M', 'occupation': 'Software Engineer'}


@pytest.mark.people
@pytest.mark.parametrize("value, expected", [
    ('M', Gender.MASCULINE), ('F', Gender.FEMININE)
])
def test_gender_value(value, expected):
    assert Gender(value) == expected


@pytest.mark.people
@pytest.mark.parametrize("value, expected", [
    (Gender.MASCULINE, 'M'), (Gender.FEMININE, 'F')
])
def test_gender_to_str(value, expected):
    assert str(value) == expected


@pytest.mark.people
def test_person_init(person):
    assert person.id == 1
    assert person.first_name == 'Tiago'
    assert person.last_name == 'Missão'
    assert person.age == 28
    assert person.gender == Gender.MASCULINE
    assert person.occupation == 'Software Engineer'


@pytest.mark.people
def test_person_repr(person):
    expected = (f'<Person(id={person.id}, first_name={person.first_name}, '
                f'last_name={person.last_name}, age={person.age} '
                f'gender={person.gender}, occupation={person.occupation})>')
    assert str(person) == expected


@pytest.mark.people
def test_person_eq(person):
    clone = Person(person.id, person.first_name, person.last_name,
                   person.age, person.gender, person.occupation)
    assert person == clone


@pytest.mark.people
def test_person_eq_diff(person):
    clone = Person(5, person.first_name, person.last_name,
                   person.age, person.gender, person.occupation)
    assert not person == clone


@pytest.mark.people
def test_personschema_to_person(person_schema, person_schema_data, person):
    assert person_schema.make_person(person_schema_data) == person
