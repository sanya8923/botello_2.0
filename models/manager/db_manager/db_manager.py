from abc import ABC, abstractmethod


class DbManager(ABC):
    pass

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

















