from models.manager.db_manager.db_manager import DbManager
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorDatabase


class ChatDbManager(DbManager):
    def __init__(self):
        super().__init__()

    async def add(self):  # abstract method
        pass

    async def update(self):  # abstract method
        pass

    async def get(self):  # abstract method
        pass

    async def find_from_id(self):  # abstract method
        pass

    async def find_from_username(self):  # abstract method
        pass


class PrivateChatDbManager(DbManager):
    def __init__(self):
        super().__init__()

    async def add(self):  # abstract method
        pass

    async def update(self):  # abstract method
        pass

    async def get(self):  # abstract method
        pass

    async def find_from_id(self):  # abstract method
        pass

    async def find_from_username(self):  # abstract method
        pass


class PrivateChatMongoDbManager(PrivateChatDbManager):
    def __init__(self):
        super().__init__()

    async def add(self):  # TODO: add method
        pass

    async def update(self):  # TODO: add method
        pass

    async def get(self):  # TODO: add method
        pass

    async def find_from_id(self):  # TODO: add method
        pass

    async def find_from_username(self):  # TODO: add method
        pass


class PublicChatDbManager(DbManager):
    def __init__(self):
        super().__init__()

    async def add(self):  # abstract method
        pass

    async def update(self):  # abstract method
        pass

    async def get(self):  # abstract method
        pass

    async def find_from_id(self):  # abstract method
        pass

    async def find_from_username(self):  # abstract method
        pass


class PublicChatMongoDbManager(PublicChatDbManager):
    def __init__(self):
        super().__init__()

    async def add(self):  # TODO: add method
        pass

    async def update(self):  # TODO: add method
        pass

    async def get(self):  # TODO: add method
        pass

    async def find_from_id(self):  # TODO: add method
        pass

    async def find_from_username(self):  # TODO: add method
        pass

