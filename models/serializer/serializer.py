from models.objects.user import User
from models.objects.chat import Chat
from models.objects.update import UpdateData
from typing import Union
from abc import ABC, abstractmethod
from colorama import init, Fore
import json
from models.base_module import Base
import logger

init(autoreset=True)


class Serializer(ABC, Base):
    def __init__(self):
        super().__init__()


    @abstractmethod
    @logger.MyLogger(name='log').log_method_info
    async def to_dict(self, obj: Union[User, Chat, UpdateData]) -> dict:
        pass

    @abstractmethod
    @logger.MyLogger(name='log').log_method_info
    async def from_json(self):
        pass

    @abstractmethod
    @logger.MyLogger(name='log').log_method_info
    async def from_dict(self):
        pass

    @logger.MyLogger(name='log').log_method_info
    async def add_to_dict(self, json_object: str, data: dict):

        with open(f'{json_object}', 'w') as file:
            json.dump(data, file, separators=(',\n', ': '))
