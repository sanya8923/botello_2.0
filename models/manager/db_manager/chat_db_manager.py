from models.manager.db_manager.db_manager import DbManager


class ChatDbManager(DbManager):
    async def add(self):  # abstract method
        pass


class PrivateChatDbManager(DbManager):
    async def add(self):  # abstract method
        pass


class PrivateChatMongoDbManager(PrivateChatDbManager):
    pass


class PublicChatDbManager(DbManager):
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

