from models.manager.db_manager.db_manager import DbManager
import logger


class MongoDbManager(DbManager):
    def __init__(self):
        super().__init__()
        self.db = None

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
