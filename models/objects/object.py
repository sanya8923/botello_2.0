from aiogram.types import Message, CallbackQuery
from models.base_module import Base


class Object(Base):
    def __init__(self, update: [Message, CallbackQuery]):
        super().__init__()
        self.update = update
