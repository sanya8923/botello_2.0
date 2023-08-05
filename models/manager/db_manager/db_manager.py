from abc import ABC, abstractmethod
from typing import Optional, Type
from motor.motor_asyncio import AsyncIOMotorDatabase
# from logger import MyLogger


class DbManager(ABC):
    def __init__(self):
        self._db: Optional[Type[AsyncIOMotorDatabase]]
        # self.logger: MyLogger('')

    @abstractmethod
    async def add(self):
        pass

    @abstractmethod
    async def update(self):
        pass

    @abstractmethod
    async def get(self):
        pass

    @abstractmethod
    async def find_from_id(self):
        pass

    @abstractmethod
    async def find_from_username(self):
        pass

















