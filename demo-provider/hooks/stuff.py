"""Demo hook to show how it does stuff."""

from pydantic import Field
from tackle.models import BaseHook


class Stuff(BaseHook):
    type: str = "do-stuff"
    things: str = Field(None, description="All the things.")

    _args: list = ['things']

    def execute(self):
        return self.things
