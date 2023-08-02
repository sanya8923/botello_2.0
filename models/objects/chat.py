from models.objects.object import Object
from aiogram.types import Message
from colorama import init, Fore

init(autoreset=True)


class Chat(Object):
    def __init__(self, message: Message):
        super().__init__(message)
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.id: int = message.chat.id


class PrivateChat(Chat):
    def __init__(self, message: Message):
        super().__init__(message)
        print(Fore.BLUE + f'{self.__class__.__name__}')


class PublicChat(Chat):
    def __init__(self, message: Message):
        super().__init__(message)
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.username: str = message.chat.username
        self.title: str = message.chat.title


class Group(PublicChat):
    def __init__(self, message: Message):
        super().__init__(message)
        print(Fore.BLUE + f'{self.__class__.__name__}')


class SuperGroup(PublicChat):
    def __init__(self, message: Message):
        super().__init__(message)
        print(Fore.BLUE + f'{self.__class__.__name__}')

