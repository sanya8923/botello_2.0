from models.manager.db_manager.db_manager import DbManager


class UserDbManager(DbManager):
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


class UserMongoDbManager(UserDbManager):
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

