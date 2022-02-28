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
