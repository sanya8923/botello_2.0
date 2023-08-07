from models.manager.db_manager.db_manager import DbManager
import logger
from models.objects.db import MongoDb


class MongoDbManager(DbManager):
    def __init__(self):
        super().__init__()
        self.mongo_db = MongoDb()
        self.db = self.mongo_db.db

    @logger.MyLogger(name='log').log_method_info
    async def add(self, *args, **kwargs):
        pass

    @logger.MyLogger(name='log').log_method_info
    async def update(self):
        pass

    @logger.MyLogger(name='log').log_method_info
    async def get(self):
        pass

    @logger.MyLogger(name='log').log_method_info
    async def find_from_id(self):
        pass

    @logger.MyLogger(name='log').log_method_info
    async def find_from_username(self):
        pass


class MessageMongoDbManager(MongoDbManager):
    @logger.MyLogger(name='log').log_method_info
    async def add(self, data: dict, group_id: int):

        collection = self.db[f'messages {group_id}']
        await self.mongo_db.update(collection, data)

    @logger.MyLogger(name='log').log_method_info
    async def update(self):
        pass

    @logger.MyLogger(name='log').log_method_info
    async def get(self):
        pass

    @logger.MyLogger(name='log').log_method_info
    async def find_from_id(self):
        pass

    @logger.MyLogger(name='log').log_method_info
    async def find_from_username(self):
        pass


class ChatMongoDbManager(MongoDbManager):
    @logger.MyLogger(name='log').log_method_info
    async def add(self, data: dict):

        collection = self.db['groups']
        await self.mongo_db.update(collection, data)

    @logger.MyLogger(name='log').log_method_info
    async def update(self):
        pass

    @logger.MyLogger(name='log').log_method_info
    async def get(self):
        pass

    @logger.MyLogger(name='log').log_method_info
    async def find_from_id(self):
        pass

    @logger.MyLogger(name='log').log_method_info
    async def find_from_username(self):
        pass


class UserMongoDbManager(MongoDbManager):
    @logger.MyLogger(name='log').log_method_info
    async def add(self, data: dict):

        collection = self.db['users']
        await self.mongo_db.update(collection, data)

    @logger.MyLogger(name='log').log_method_info
    async def update(self):
        pass

    @logger.MyLogger(name='log').log_method_info
    async def get(self):
        pass

    @logger.MyLogger(name='log').log_method_info
    async def find_from_id(self):
        pass

    @logger.MyLogger(name='log').log_method_info
    async def find_from_username(self):
        pass


class GroupMemberRoleMongoDbManager(MongoDbManager):

    @logger.MyLogger(name='log').log_method_info
    async def add(self, data: dict):

        collection = self.db['group_member_role']
        await self.mongo_db.update_role(collection, data)

    @logger.MyLogger(name='log').log_method_info
    async def update(self):
        pass

    @logger.MyLogger(name='log').log_method_info
    async def get(self):
        pass
    
    @logger.MyLogger(name='log').log_method_info
    async def find_from_id(self):
        pass
    
    @logger.MyLogger(name='log').log_method_info
    async def find_from_username(self):
        pass
