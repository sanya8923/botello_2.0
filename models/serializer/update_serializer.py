from models.serializer.serializer import Serializer
from aiogram.types import Message, CallbackQuery
from typing import Union, Optional
from models.objects.update import UpdateData, MessageData, MessagePublicChat, MessagePrivateChat, Callback
from colorama import init, Fore

init(autoreset=True)


class UpdateSerializer(Serializer):
    def __init__(self):
        print(Fore.BLUE + f'{self.__class__.__name__}')

    async def to_json(self, message: Message):  # abstract method
        pass

    async def from_json(self):  # abstract method
        pass

    async def from_dict(self):  # abstract method
        pass


class MessageDataSerializer(UpdateSerializer):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.id: Optional[int] = None
        self.message_text: Optional[str] = None
        self.from_user: Optional[int] = None
        self.from_chat: Optional[int] = None
        self.file: str = 'jsons/message.json'

    async def to_json(self, message: Message):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        self.id = message.message_id
        self.message_text = message.text
        self.from_user = message.from_user.id
        self.from_chat = message.chat.id

        data = {
            'id': self.id,
            'text': self.message_text,
            'from_user': self.from_user,
            'from_chat': self.from_chat
        }

        await self.add_to_json(self.file, data)

        return data

    async def from_json(self):  # TODO: add method
        pass

    async def from_dict(self):  # TODO: add method
        pass


class MessagePrivateChatSerializer(MessageDataSerializer):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')


class MessagePublicChatSerializer(MessageDataSerializer):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')


class CallbackSerializer(UpdateSerializer):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.callback_data: Optional[str] = None
