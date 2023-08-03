from typing import Optional, List
from models.objects.object import Object
from models.objects.user import User
from models.objects.chat import Chat
from aiogram.types import Message, MessageEntity, CallbackQuery
from colorama import init, Fore

init(autoreset=True)


class UpdateData(Object):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.update: Optional[Message, CallbackQuery] = None


class MessageData(UpdateData):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.message_data: Optional[Message] = None
        self.id: Optional[int] = None
        self.from_user: Optional[User] = None
        self.from_chat: Optional[Chat] = None
        self.text: Optional[str] = None
        self.entities_data: Optional[List[MessageEntity]] = None


class MessagePrivateChat(MessageData):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.for_chat: Optional[List[Chat]] = None


class MessagePublicChat(MessageData):
    def __init__(self):
        print(Fore.BLUE + f'{self.__class__.__name__}')
        super().__init__()


class Callback(UpdateData):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.callback: Optional[CallbackQuery] = None
        self.callback_data: Optional[str] = None
