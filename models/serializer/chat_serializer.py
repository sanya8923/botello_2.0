from models.serializer.serializer import Serializer
from typing import Optional
from aiogram.types import Message
from models.objects.chat import Chat, PublicChat, PrivateChat, Group, SuperGroup
from colorama import init, Fore

init(autoreset=True)


class ChatSerializer(Serializer):
    def __init__(self):
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.chat_id: Optional[int] = None

    async def to_json(self, message: Message):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        self.chat_id = message.chat.id
        data = {'id': self.chat_id}

        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass


class PrivateChatSerializer(ChatSerializer):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.file: str = 'jsons/private_chat.json'
        self.chat_type: str = 'private'

    async def to_json(self, message: Message):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        data = await super().to_json(message)
        data['type'] = self.chat_type
        await self.add_to_json(self.file, data)

        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass


class PublicChatSerializer(ChatSerializer):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.username: Optional[str] = None
        self.title: Optional[str] = None
        self.file: str = 'jsons/public_chat.json'

    async def to_json(self, message: Message):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        data = await super().to_json(message)

        self.username = message.chat.username
        self.title = message.chat.title

        data['username'] = self.username
        data['title'] = self.title
        await self.add_to_json(self.file, data)

        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass


class GroupSerializer(PublicChatSerializer):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.chat_type: str = 'group'

    async def to_json(self, message: Message):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        data = await super().to_json(message)
        data['type'] = self.chat_type
        await self.add_to_json(self.file, data)

        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass


class SuperGroupSerializer(PublicChatSerializer):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.chat_type: str = 'supergroup'

    async def to_json(self, message: Message):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        data = await super().to_json(message)
        data['type'] = self.chat_type
        await self.add_to_json(self.file, data)

        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass
