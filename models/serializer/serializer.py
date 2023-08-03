from aiogram.types import Message
from abc import ABC, abstractmethod
from colorama import init, Fore
from typing import IO
import json

init(autoreset=True)


class Serializer(ABC):
    def __init__(self, message: Message):
        self.message = message

    @abstractmethod
    async def to_json(self):
        pass

    @abstractmethod
    async def from_json(self):
        pass

    @abstractmethod
    async def from_message(self):
        pass

    async def add_to_json(self, json_object: str, data: dict):
        print(Fore.LIGHTYELLOW_EX + f'{self.add_to_json.__name__} in class {self.__class__.__name__}')

        with open(f'{json_object}', 'w') as file:
            json.dump(data, file, separators=(',\n', ': '))
