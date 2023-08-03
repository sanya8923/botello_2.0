from aiogram.types import Message, CallbackQuery
from abc import ABC, abstractmethod
from colorama import init, Fore
from typing import IO, Union
import json

init(autoreset=True)


class Serializer(ABC):
    @abstractmethod
    async def to_json(self, update: Union[Message, CallbackQuery]):
        pass

    @abstractmethod
    async def from_json(self):
        pass

    @abstractmethod
    async def from_dict(self):
        pass

    async def add_to_json(self, json_object: str, data: dict):
        print(Fore.LIGHTYELLOW_EX + f'{self.add_to_json.__name__} in class {self.__class__.__name__}')

        with open(f'{json_object}', 'w') as file:
            json.dump(data, file, separators=(',\n', ': '))
