from typing import Optional
from abc import ABC, abstractmethod


class Object(ABC):
    def __init__(self):
        self.id: Optional[int] = None

    @abstractmethod
    async def to_json(self):
        pass

    @abstractmethod
    async def from_json(self):
        pass


