from typing import Optional, List, Union
from models.objects.object import Object
from models.objects.user import User
from models.objects.chat import Chat
from aiogram.types import Message, MessageEntity, CallbackQuery


class Update(Object):
    def __init__(self, update: Union[Message, CallbackQuery]):
        super().__init__()
        self.id: int = update.message.message_id
        self.from_user: User = User(update)
        self.from_chat: Chat = Chat(update)


class MessageData(Update):
    def __init__(self, message: Message):
        super().__init__(message)
        self.message_data: Message = message
        self.text: str = message.text
        self.entities_data: Optional[List[MessageEntity]] = message.entities


class MessagePrivateChat(MessageData):
    def __init__(self, message: Message):
        super().__init__(message)
        self.for_chat: Optional[List[Chat]]


class MessagePublicChat(MessageData):
    def __init__(self, message: Message):
        super().__init__(message)


class Callback(Update):
    def __init__(self, callback: CallbackQuery):
        super().__init__(callback)
        self.callback: CallbackQuery = callback
        self.callback_data = callback.data
