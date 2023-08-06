from models.objects.object import Object
from typing import Optional, Union
from aiogram.types import Message, CallbackQuery


class User(Object):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)
        self.id: int = self.update.from_user.id
        self.username: str = self.update.from_user.username
        self.first_name: str = self.update.from_user.first_name
        self.last_name: str = self.update.from_user.last_name
        self.new_member: bool = False  # TODO: когда будет готово подключение к БД добей сюда функцию


class Member(User):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)


class Admin(Member):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)


class Creator(Member):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)


class NotMember(User):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)


class MemberKicked(NotMember):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)


class MemberLeft(NotMember):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)
