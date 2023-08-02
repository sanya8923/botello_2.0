from models.serializer.serializer import Serializer
from models.objects.chat import Chat, PublicChat, PrivateChat, Group, SuperGroup
from colorama import init, Fore

init(autoreset=True)


class ChatSerializer(Serializer):
    def __init__(self, chat: Chat):
        super().__init__(chat)
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.chat_id: int = chat.id

    async def to_json(self):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        data = {'id': self.chat_id}

        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass


class PrivateChatSerializer(ChatSerializer):
    def __init__(self, chat: PrivateChat):
        super().__init__(chat)
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.file: str = 'jsons/private_chat.json'
        self.chat_type: str = 'private'

    async def to_json(self):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json().__name__} in class {self.__class__.__name__}')

        data = await super().to_json()
        data['type'] = self.chat_type
        await self.add_to_json(self.file, data)

        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass


class PublicChatSerializer(ChatSerializer):
    def __init__(self, chat: PublicChat):
        super().__init__(chat)
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.username: int = chat.username
        self.title: str = chat.title
        self.file: str = 'jsons/public_chat.json'

    async def to_json(self):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        data = await super().to_json()
        data['username'] = self.username
        data['title'] = self.title
        await self.add_to_json(self.file, data)

        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass


class GroupSerializer(PublicChatSerializer):
    def __init__(self, chat: Group):
        super().__init__(chat)
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.chat_type: str = 'group'

    async def to_json(self):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        data = await super().to_json()
        data['type'] = self.chat_type
        await self.add_to_json(self.file, data)

        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass


class SuperGroupSerializer(PublicChatSerializer):
    def __init__(self, chat: SuperGroup):
        super().__init__(chat)
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.chat_type: str = 'supergroup'

    async def to_json(self):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        data = await super().to_json()
        data['type'] = self.chat_type
        await self.add_to_json(self.file, data)

        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass
