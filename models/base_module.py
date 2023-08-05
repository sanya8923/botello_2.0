from logger import MyLogger

logger = MyLogger('my_logger')


class Base:
    def __init__(self, *args, **kwargs):
        self.logger = logger
