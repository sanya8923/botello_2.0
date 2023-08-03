from models.objects.user import User
from models.objects.chat import Chat
from models.objects.update import UpdateData
from typing import Union
from abc import ABC, abstractmethod
from colorama import init, Fore
import json

init(autoreset=True)


class Serializer(ABC):
    @abstractmethod
    async def to_json(self, obj: Union[User, Chat, UpdateData]) -> dict:
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
