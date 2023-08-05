from abc import ABC, abstractmethod
from typing import Optional, Type
from motor.motor_asyncio import AsyncIOMotorDatabase
from models.manager.manager import Manager
import logger


class DbManager(ABC, Manager):
    @logger.MyLogger(name='log').log_class_info
    def __init__(self):
        super().__init__()
        self._db: Optional[Type[AsyncIOMotorDatabase]]

    @abstractmethod
    @logger.MyLogger(name='log').log_method_info
    async def add(self):
        pass

    @abstractmethod
    @logger.MyLogger(name='log').log_method_info
    async def update(self):
        pass

    @abstractmethod
    @logger.MyLogger(name='log').log_method_info
    async def get(self):
        pass

    @abstractmethod
    @logger.MyLogger(name='log').log_method_info
    async def find_from_id(self):
        pass

    @abstractmethod
    @logger.MyLogger(name='log').log_method_info
    async def find_from_username(self):
        pass

















