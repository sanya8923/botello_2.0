from aiogram.types import Message


class Object:
    def __init__(self, message: Message):
        self.message: Message = message
