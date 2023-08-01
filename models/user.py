from typing import Optional
from models.object import Object
from aiogram.types import Message


class User(Object):
    def __init__(self, message: Message):
        super().__init__()
        self.id: int = message.from_user.id
        self.username: str = message.from_user.username
        self.first_name: str = message.from_user.first_name
        self.last_name: str = message.from_user.last_name


class Member(User):
    pass


class NewMember(Member):
    pass


class MiddleMember(Member):
    pass


class Admin(Member):
    pass


class Creator(Member):
    pass


class NotMember(User):
    pass


class Kicked(NotMember):
    pass


class Left(NotMember):
    pass
