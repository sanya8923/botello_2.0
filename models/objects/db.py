import motor.motor_asyncio
import config_reader


cluster = motor.motor_asyncio.AsyncIOMotorClient(config_reader.config.mongo_db.get_secret_value())
db = cluster['db']


class Db:
    def __init__(self):
        self.mongo_db = db


class MongoDb(Db):
    def __init__(self):
        super().__init__()
        self.db = self.mongo_db

