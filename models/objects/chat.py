from models.objects.object import Object
from colorama import init, Fore
from typing import Optional

init(autoreset=True)


class Chat(Object):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.id: Optional[int] = None


class PrivateChat(Chat):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')


class PublicChat(Chat):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.username: Optional[str] = None
        self.title: Optional[str] = None


class Group(PublicChat):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')


class SuperGroup(PublicChat):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')

