from models.object import Object
from abc import ABC, abstractmethod


class Serializer(ABC):
    def __init__(self, obj: Object):
        self.object = obj

    @abstractmethod
    async def to_json(self):
        pass

    @abstractmethod
    async def from_json(self):
        pass
