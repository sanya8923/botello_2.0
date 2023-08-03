from aiogram.types import Message
from colorama import Fore, init
from abc import ABC, abstractmethod
from typing import Optional

from models.objects.user import Creator
from models.serializer.user_serializer import CreatorSerializer

from models.objects.chat import Group
from models.serializer.chat_serializer import GroupSerializer

from models.objects.update import MessagePublicChat
from models.serializer.update_serializer import MessagePublicChatSerializer

from models.serializer.group_member_role_serializer import GroupMemberRoleSerializer

init(autoreset=True)


class NewMessageManager(ABC):
    def __init__(self, message: Message):
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.message = message

@abstractmethod
    async def serialize(self):
        pass


