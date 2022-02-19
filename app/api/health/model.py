import datetime
from marshmallow import Schema, fields, post_load


class Health:

    def __init__(self) -> None:
        self.running = True
        self.date = datetime.datetime.now()
        self.version = "0.0.1"

    def __repr__(self):
        return (f'<Health(running={self.running}, date={self.date}, '
                f'version={self.version})>')


class HealthSchema(Schema):
    running = fields.Boolean()
    date = fields.DateTime()
    version = fields.Str()

    # pylint: disable=unused-argument
    @post_load
    def make_health(self, data, **kwargs) -> Health:
        return Health(**data)
    # pylint: enable=unused-argument
