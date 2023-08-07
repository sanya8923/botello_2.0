from logger import MyLogger

from colorama import Fore, init

init(autoreset=True)
logger = MyLogger('my_logger')


class Base:
    def __init__(self, *args, **kwargs):
        print(Fore.LIGHTYELLOW_EX + f'{self.__class__.__name__}')
        self.logger = logger
