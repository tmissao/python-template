from enum import Enum
from marshmallow import Schema, fields, post_load


class Gender(Enum):
    MASCULINE = "M"
    FEMININE = "F"

    def __str__(self):
        return self.value


class Person:

    def __init__(self, id, first_name, last_name, age, gender,
                 occupation) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = Gender(gender)
        self.occupation = occupation

    def __repr__(self):
        return (f'<Person(id={self.id}, first_name={self.first_name}, '
                f'last_name={self.last_name}, age={self.age} '
                f'gender={self.gender}, occupation={self.occupation})>')

    def __eq__(self, other):
        return (self.id == other.id and
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.age == other.age and
                self.gender == other.gender and
                self.occupation == other.occupation)


class PersonSchema(Schema):
    id = fields.Int(missing=None, default=None)
    first_name = fields.Str(data_key="firstName")
    last_name = fields.Str(data_key="lastName")
    age = fields.Int()
    gender = fields.Str()
    occupation = fields.Str(missing=None, default=None)

    # pylint: disable=unused-argument
    @post_load
    def make_person(self, data, **kwargs) -> Person:
        return Person(**data)
    # pylint: enable=unused-argument


class PersonPatchSchema(Schema):
    first_name = fields.Str(data_key="firstName")
    last_name = fields.Str(data_key="lastName")
    age = fields.Int()
    gender = fields.Str()
    occupation = fields.Str(missing=None, default=None, allow_none=True)
