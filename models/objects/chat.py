from models.objects.object import Object
from colorama import init, Fore
from typing import Optional, Union
from aiogram.types import Message, CallbackQuery

init(autoreset=True)


class Chat(Object):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)
        print(Fore.BLUE + f'{self.__class__.__name__}')

        if isinstance(self.update, Message):
            self.id: int = self.update.message_id
        else:
            self.id: int = self.update.id


class PrivateChat(Chat):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)
        print(Fore.BLUE + f'{self.__class__.__name__}')


class PublicChat(Chat):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)
        print(Fore.BLUE + f'{self.__class__.__name__}')
        if isinstance(self.update, Message):
            self.username: str = self.update.chat.username
            self.title: str = self.update.chat.title
        else:
            self.username: str = self.update.message.chat.username
            self.title: str = self.update.message.chat.title


class Group(PublicChat):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)
        print(Fore.BLUE + f'{self.__class__.__name__}')


class SuperGroup(PublicChat):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)
        print(Fore.BLUE + f'{self.__class__.__name__}')

