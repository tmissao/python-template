# from flask import Blueprint

# NAMESPACE = 'health'
# blueprint = Blueprint(NAMESPACE, __name__)


# @blueprint.route('/')
# def health():
#     return 'up', 200


# def get_blueprint():
#     return {"blueprint": blueprint, "prefix": f'/{NAMESPACE}'}

from typing import Tuple
from flask import Blueprint, jsonify

from .model import HealthSchema, Health
from ...interfaces.api import BaseAPI


class HealthAPI(BaseAPI):

    NAMESPACE = 'health'
    BLUEPRINT = blueprint = Blueprint(NAMESPACE, __name__)

    @staticmethod
    @blueprint.route('/')
    def health():
        print(Health())
        return jsonify(HealthSchema().dump(Health()))

    @staticmethod
    def get_blueprint() -> Blueprint:
        return HealthAPI.BLUEPRINT

    @staticmethod
    def get_prefix() -> str:
        return f'/{HealthAPI.NAMESPACE}'

    @staticmethod
    def get_register_blueprint() -> Tuple[Blueprint, str]:
        return HealthAPI.get_blueprint(), HealthAPI.get_prefix()
