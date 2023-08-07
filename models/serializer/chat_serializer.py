from models.serializer.serializer import Serializer
from typing import Optional
from aiogram.types import Message
from models.objects.chat import Chat, PublicChat, PrivateChat, Group, SuperGroup
import logger


class ChatSerializer(Serializer):
    def __init__(self):
        super().__init__()
        self.chat_id: Optional[int] = None

    @logger.MyLogger(name='log').log_method_info
    async def to_dict(self, chat: Chat) -> dict:

        self.chat_id = chat.id
        data = {'id': self.chat_id}

        return data

    @logger.MyLogger(name='log').log_method_info
    async def from_json(self):  # TODO: add method
        pass

    @logger.MyLogger(name='log').log_method_info
    async def from_dict(self):  # TODO: add method
        pass


class PrivateChatSerializer(ChatSerializer):
    def __init__(self):
        super().__init__()

        self.file: str = 'jsons/private_chat.json'
        self.chat_type: str = 'private'

    async def to_dict(self, chat: PrivateChat) -> dict:
        data = await super().to_dict(chat)
        data['type'] = self.chat_type

        return data

    async def from_json(self):  # TODO: add method
        pass

    async def from_dict(self):  # TODO: add method
        pass


class PublicChatSerializer(ChatSerializer):
    def __init__(self):
        super().__init__()

        self.username: Optional[str] = None
        self.title: Optional[str] = None
        self.file: str = 'jsons/public_chat.json'

    @logger.MyLogger(name='log').log_method_info
    async def to_dict(self, chat: PublicChat) -> dict:

        data = await super().to_dict(chat)

        self.username = chat.username
        self.title = chat.title

        data['username'] = self.username
        data['title'] = self.title

        return data

    @logger.MyLogger(name='log').log_method_info
    async def from_json(self):  # TODO: add method
        pass

    @logger.MyLogger(name='log').log_method_info
    async def from_dict(self):  # TODO: add method
        pass


class GroupSerializer(PublicChatSerializer):
    def __init__(self):
        super().__init__()

        self.chat_type: str = 'group'

    async def to_dict(self, group: Group):

        data = await super().to_dict(group)
        data['type'] = self.chat_type

        return data

    async def from_json(self):  # TODO: add method
        pass

    async def from_dict(self):  # TODO: add method
        pass


class SuperGroupSerializer(PublicChatSerializer):
    def __init__(self):
        super().__init__()

        self.chat_type: str = 'supergroup'

    async def to_dict(self, group: SuperGroup):

        data = await super().to_dict(group)
        data['type'] = self.chat_type

        return data

    async def from_json(self):  # TODO: add method
        pass

    async def from_dict(self):  # TODO: add method
        pass
