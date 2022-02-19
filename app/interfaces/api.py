from abc import ABC, abstractmethod
from typing import Tuple
from flask import Blueprint


class BaseAPI(ABC):

    @staticmethod
    @abstractmethod
    def get_blueprint() -> Blueprint:
        pass

    @staticmethod
    @abstractmethod
    def get_prefix() -> str:
        pass

    @staticmethod
    @abstractmethod
    def get_register_blueprint() -> Tuple[Blueprint, str]:
        pass
