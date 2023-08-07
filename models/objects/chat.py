from models.objects.object import Object
from typing import Union
from aiogram.types import Message, CallbackQuery


class Chat(Object):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)

        self.id: int = self.update.chat.id


class PrivateChat(Chat):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)


class PublicChat(Chat):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)
        if isinstance(self.update, Message):
            self.username: str = self.update.chat.username
            self.title: str = self.update.chat.title
        else:
            self.username: str = self.update.message.chat.username
            self.title: str = self.update.message.chat.title


class Group(PublicChat):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)


class SuperGroup(PublicChat):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)

