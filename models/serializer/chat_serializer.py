from models.serializer.serializer import Serializer
from models.objects.chat import Chat, PublicChat, PrivateChat, Group, SuperGroup
from colorama import init, Fore

init(autoreset=True)


class ChatSerializer(Serializer):
    def __init__(self, chat: Chat):
        super().__init__(chat)
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.chat_id = chat.id

    async def to_json(self):  # abstract method
        pass

    async def from_json(self):  # abstract method
        pass


class PrivateChatSerializer(ChatSerializer):
    def __init__(self, chat: PrivateChat):
        super().__init__(chat)
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.chat_type: str = 'private'

    async def to_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        data = {
            'id': self.chat_id,
            'type': self.chat_type
        }
        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass


class PublicChatSerializer(ChatSerializer):
    def __init__(self, chat: PublicChat):
        super().__init__(chat)
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.username = chat.username
        self.title = chat.title

    async def to_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')
        pass

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass


class GroupSerializer(PublicChatSerializer):
    def __init__(self, chat: Group):
        super().__init__(chat)
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.chat_type: str = 'group'


class SuperGroupSerializer(PublicChatSerializer):
    def __init__(self, chat: SuperGroup):
        super().__init__(chat)
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.chat_type: str = 'supergroup'

