from aiogram.types import Message, CallbackQuery
from typing import Union


class Object:
    def __init__(self, update: [Message, CallbackQuery]):
        self.update = update
