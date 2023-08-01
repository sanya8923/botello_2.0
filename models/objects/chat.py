from models.objects.object import Object
from aiogram.types import Message


class Chat(Object):
    def __init__(self, message: Message):
        super().__init__()
        self.id: int = message.chat.id


class PrivateChat(Chat):
    pass


class PublicChat(Chat):
    def __init__(self, message: Message):
        super().__init__()
        self.username: str = message.chat.username
        self.title: str = message.chat.title


class Group(PublicChat):
    pass


class SuperGroup(PublicChat):
    pass

