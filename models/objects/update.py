from typing import Optional, List, Union
from models.objects.object import Object
from models.objects.user import User
from models.objects.chat import Chat
from aiogram.types import Message, MessageEntity, CallbackQuery


class UpdateData(Object):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__(update)


class MessageData(UpdateData):
    def __init__(self, message: Message):
        super().__init__(message)

        self.id: int = self.update.message_id
        self.from_user: User = self.update.from_user
        self.from_chat: Chat = self.update.chat
        self.text: str = self.update.text
        self.entities_data: Optional[List[MessageEntity]] = self.update.entities
        self.date = self.update.date


class MessagePrivateChat(MessageData):
    def __init__(self, message: Message):
        super().__init__(message)
        self.for_chat: Optional[List[Chat]] = None


class MessagePublicChat(MessageData):
    def __init__(self, message: Message):
        super().__init__(message)


class Callback(UpdateData):
    def __init__(self, callback: CallbackQuery):
        super().__init__(callback)
        self.callback_data: str = callback.data
