from abc import ABC, abstractmethod
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorDatabase
import config_reader
from typing import Optional, Type
from colorama import init, Fore

init(autoreset=True)


cluster = motor.motor_asyncio.AsyncIOMotorClient(config_reader.config.bot_token.get_secret_value())
db = cluster['db']


class Db(ABC):
    def __init__(self):
        self.db: Optional[Type[Type[AsyncIOMotorDatabase]]]  # add new type when you add new databases
        print(Fore.YELLOW + 'DB RUN')

    @abstractmethod
    async def plug(self):
        pass


class MongoDb(Db):
    def __init__(self):
        super().__init__()


    async def plug(self):
        pass
