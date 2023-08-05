from abc import ABC, abstractmethod
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorDatabase
import config_reader
from typing import Optional, Type
from colorama import init, Fore
import logger

init(autoreset=True)


cluster = motor.motor_asyncio.AsyncIOMotorClient(config_reader.config.bot_token.get_secret_value())
db = cluster['db']


class Db(ABC):
    @logger.MyLogger(name='log').log_class_info
    def __init__(self):
        self.db: Optional[Type[Type[AsyncIOMotorDatabase]]]  # add new type when you add new databases
        print(Fore.YELLOW + 'DB RUN')

    @abstractmethod
    @logger.MyLogger(name='log').log_method_info
    async def plug(self):
        pass


class MongoDb(Db):
    def __init__(self):
        super().__init__()


    async def plug(self):
        pass
