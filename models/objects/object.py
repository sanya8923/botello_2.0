from aiogram.types import TelegramObject


class Object:
    def __init__(self, obj: TelegramObject):
        self.object = obj
