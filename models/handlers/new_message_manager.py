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


class NewMessageFromCreatorManager(NewMessageManager):
    def __init__(self, message: Message):
        super().__init__(message)
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.message_data = MessagePublicChat(self.message)
        self.creator = Creator(self.message)
        self.group = Group(self.message)

        self.message_data_dict: Optional[dict] = None
        self.group_dict: Optional[dict] = None
        self.creator_dict: Optional[dict] = None
        self.group_member_role_dict: Optional[dict] = None

    async def serialize(self):
        print(Fore.LIGHTYELLOW_EX + f'{self.serialize.__name__} in class {self.__class__.__name__}')

        message_serializer = MessagePublicChatSerializer()
        creator_serializer = CreatorSerializer()
        group_serializer = GroupSerializer()
        group_member_role_serializer = GroupMemberRoleSerializer()

        self.message_data_dict = await message_serializer.to_json(self.message_data)  # return dict (don't use) with message data and save json
        self.creator_dict = await creator_serializer.to_json(self.creator)  # return dict (don't use) with member data and save json
        self.group_dict = await group_serializer.to_json(self.group)  # return dict (don't use) with group data and save json
        self.group_member_role_dict = await group_member_role_serializer.to_json(self.message_data)  # return dict (don't use) with group_id, user_id and role and save json


