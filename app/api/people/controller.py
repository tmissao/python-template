from typing import Tuple
from flask import Blueprint, jsonify, request, abort
from .model import PersonPatchSchema, PersonSchema
from .domain import PersonDomain
from ...interfaces.api import BaseAPI


class PersonAPI(BaseAPI):

    NAMESPACE = 'people'
    BLUEPRINT = blueprint = Blueprint(NAMESPACE, __name__)
    DOMAIN = PersonDomain()

    @staticmethod
    @blueprint.route('/<int:person_id>', methods=['GET'])
    def get_person(person_id):
        try:
            person = PersonAPI.DOMAIN.get(person_id)
            return jsonify(PersonSchema().dump(person)), 200
        except ValueError as error:
            return abort(404, error)

    @staticmethod
    @blueprint.route('/list', methods=['GET'])
    def get_people():
        people = PersonAPI.DOMAIN.get_all()
        return jsonify(PersonSchema(many=True).dump(people)), 200

    @staticmethod
    @blueprint.route('/<int:person_id>', methods=['PUT'])
    def update_person(person_id):
        schema = PersonSchema()
        person = schema.load(request.get_json())
        person.id = person_id
        try:
            PersonAPI.DOMAIN.replace(person)
        except ValueError as error:
            return abort(404, error)
        return jsonify(schema.dump(person)), 200

    @staticmethod
    @blueprint.route('/<int:person_id>', methods=['PATCH'])
    def patch_person(person_id):
        patch = PersonPatchSchema().load(request.get_json())
        try:
            person = PersonAPI.DOMAIN.update(person_id, **patch)
            return jsonify(PersonSchema().dump(person)), 200
        except ValueError as error:
            return abort(404, error)

    @staticmethod
    @blueprint.route('/', methods=['POST'])
    def add_person():
        schema = PersonSchema()
        person = schema.load(request.get_json())
        try:
            PersonAPI.DOMAIN.add(person)
        except ValueError as error:
            return abort(404, error)

        return jsonify(schema.dump(person)), 201

    @staticmethod
    @blueprint.route('/<int:person_id>', methods=['DELETE'])
    def delete_person(person_id):
        try:
            PersonAPI.DOMAIN.delete(person_id), 200
        except ValueError as error:
            return abort(404, error)
        return "", 204

    @staticmethod
    def get_blueprint() -> Blueprint:
        return PersonAPI.BLUEPRINT

    @staticmethod
    def get_prefix() -> str:
        return f'/{PersonAPI.NAMESPACE}'

    @staticmethod
    def get_register_blueprint() -> Tuple[Blueprint, str]:
        return PersonAPI.get_blueprint(), PersonAPI.get_prefix()
