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

    async def to_json(self, chat: Chat):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        self.chat_id = chat.id
        data = {'id': self.chat_id}

        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass

    async def from_dict(self):  # TODO: add method
        pass


class PrivateChatSerializer(ChatSerializer):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.file: str = 'jsons/private_chat.json'
        self.chat_type: str = 'private'

    async def to_json(self, chat: PrivateChat):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        data = await super().to_json(chat)
        data['type'] = self.chat_type
        await self.add_to_json(self.file, data)

        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass

    async def from_dict(self):  # TODO: add method
        pass


class PublicChatSerializer(ChatSerializer):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.username: Optional[str] = None
        self.title: Optional[str] = None
        self.file: str = 'jsons/public_chat.json'

    async def to_json(self, chat: PublicChat):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        data = await super().to_json(chat)

        self.username = chat.username
        self.title = chat.title

        data['username'] = self.username
        data['title'] = self.title
        await self.add_to_json(self.file, data)

        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass

    async def from_dict(self):  # TODO: add method
        pass


class GroupSerializer(PublicChatSerializer):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.chat_type: str = 'group'

    async def to_json(self, group: Group):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        data = await super().to_json(group)
        data['type'] = self.chat_type
        await self.add_to_json(self.file, data)

        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass

    async def from_dict(self):  # TODO: add method
        pass


class SuperGroupSerializer(PublicChatSerializer):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.chat_type: str = 'supergroup'

    async def to_json(self, group: SuperGroup):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        data = await super().to_json(group)
        data['type'] = self.chat_type
        await self.add_to_json(self.file, data)

        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass

    async def from_dict(self):  # TODO: add method
        pass
