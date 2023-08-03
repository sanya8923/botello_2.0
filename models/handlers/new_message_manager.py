from aiogram.types import Message
from colorama import Fore, init
from abc import ABC, abstractmethod
from typing import Optional, Union

from models.objects.user import Creator, Admin, Member
from models.serializer.user_serializer import CreatorSerializer, AdminSerializer, MemberSerializer

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

        self.message_data: Optional[MessagePublicChat] = None
        self.user: Optional[Creator] = None
        self.group: Optional[Group] = None

        self.message_serializer: Optional[MessagePublicChatSerializer] = None
        self.user_serializer: Optional[CreatorSerializer] = None
        self.group_serializer: Optional[GroupSerializer] = None
        self.group_member_role_serializer: Optional[GroupMemberRoleSerializer] = None

        self.message_data_dict: Optional[dict] = None
        self.group_dict: Optional[dict] = None
        self.creator_dict: Optional[dict] = None
        self.group_member_role_dict: Optional[dict] = None

    @abstractmethod
    async def serialize(self):
        pass

    async def serialize_process(self):
        print(Fore.LIGHTYELLOW_EX + f'{self.serialize_process.__name__} in class {self.__class__.__name__}')

        self.message_data_dict = await self.message_serializer.to_json(
            self.message_data)  # return dict (don't use) with message data and save json
        self.creator_dict = await self.user_serializer.to_json(
            self.user)  # return dict (don't use) with member data and save json
        self.group_dict = await self.group_serializer.to_json(
            self.group)  # return dict (don't use) with group data and save json
        self.group_member_role_dict = await self.group_member_role_serializer.to_json(
            self.message_data)  # return dict (don't use) with group_id, user_id and role and save json


class NewMessageFromCreatorManager(NewMessageManager):
    def __init__(self, message: Message):
        super().__init__(message)
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.message_data = MessagePublicChat(self.message)
        self.creator = Creator(self.message)
        self.group = Group(self.message)

    async def serialize(self):
        print(Fore.LIGHTYELLOW_EX + f'{self.serialize.__name__} in class {self.__class__.__name__}')

        self.message_serializer = MessagePublicChatSerializer()
        self.user_serializer = CreatorSerializer()
        self.group_serializer = GroupSerializer()
        self.group_member_role_serializer = GroupMemberRoleSerializer()

        await self.serialize_process()






