from abc import ABC, abstractmethod
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorDatabase
import config_reader
from typing import Optional, Type
from colorama import init, Fore
import logger
from models.base_module import Base

init(autoreset=True)


cluster = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://sanya8923:17XS7eoFcAtELvlx@cluster0.lzxiped.mongodb.net/db?retryWrites=true&w=majority')
db = cluster['db']


class Db(ABC, Base):
    def __init__(self):
        super().__init__()
        self.db: Optional[Type[Type[AsyncIOMotorDatabase]]]  # add new type when you add new databases

    @abstractmethod
    @logger.MyLogger(name='log').log_method_info
    async def add(self, *args, **kwargs):
        pass

    @abstractmethod
    @logger.MyLogger(name='log').log_method_info
    async def update(self, *args, **kwargs):
        pass

    @abstractmethod
    @logger.MyLogger(name='log').log_method_info
    async def update_role(self, *args, **kwargs):
        pass


class MongoDb(Db):
    def __init__(self):
        super().__init__()
        self.db = db

    @logger.MyLogger(name='log').log_method_info
    async def add(self, col_name, data: dict) -> None:

        collection = self.db[col_name]
        collection[col_name].insert_one(data)

    @logger.MyLogger(name='log').log_method_info
    async def update(self, collection, data: dict):
        count = await collection.count_documents({'id': data['id']})
        if count == 0:
            collection.insert_one(data)
        else:
            delete_filter = {'id': data['id']}
            collection.delete_many(delete_filter)
            collection.insert_one(data)

    @logger.MyLogger(name='log').log_method_info
    async def update_role(self, collection, data: dict) -> None:

        filter_db = {'user_id': data['user_id'], 'chat_id': data['chat_id']}

        count = await collection.count_documents(filter_db)
        if count == 0:
            collection.insert_one(data)
        else:
            collection.delete_many(filter_db)
            collection.insert_one(data)
