from collections import defaultdict
from typing import Dict, List
import random
from .model import Person


class PersonDomain:

    def __init__(self):
        self.database: Dict[Person] = defaultdict(lambda: None)

    def __find(self, id):
        return self.database[id]

    def get_all(self) -> List[Person]:
        return self.database.values()

    def get(self, id) -> Person:
        person = self.__find(id)
        if not person:
            raise ValueError(f'Person with id {id} does not exist')
        return person

    def add(self, person) -> Person:
        if person.id:
            if self.__find(person.id):
                raise ValueError(f'Person with id {person.id} already exists')
        else:
            random_id = random.randint(1, 1000)
            while self.__find(random_id):
                random_id = random.randint(1, 1000)
            person.id = random_id
        self.database[person.id] = person
        return person

    def replace(self, person) -> Person:
        if not self.__find(person.id):
            raise ValueError(f'Person with id {person.id} does not exist')
        self.database[person.id] = person
        return person

    def update(self, id, **kwargs) -> Person:
        person = self.__find(id)
        if not person:
            raise ValueError(f'Person with id {id} does not exist')
        for key, value in kwargs.items():
            person.__dict__[key] = value
        self.database[id] = person
        return person

    def delete(self, id) -> bool:
        if not self.__find(id):
            raise ValueError(f'Person with id {id} does not exist')
        self.database.pop(id)
        return True
