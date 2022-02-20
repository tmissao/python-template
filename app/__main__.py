from typing import List
from flask import Flask
from .interfaces.api import BaseAPI
from .api.health.controller import HealthAPI
from .api.people.controller import PersonAPI
from .commons.fibonacci import Fibonacci


def run():
    fibonacci = Fibonacci()
    print('Hello from python!')
    print(fibonacci.get_random_fibonacci())
    print(fibonacci.get_multiple_random_fibonacci())
    return fibonacci.get_fibonacci(8)


def start():
    app = Flask(__name__)
    apis: List[BaseAPI] = [HealthAPI, PersonAPI]

    for e in apis:
        blueprint, prefix = e.get_register_blueprint()
        app.register_blueprint(blueprint, url_prefix=prefix)

    app.run(host="0.0.0.0", debug=True)


if __name__ == '__main__':
    # run()
    start()
