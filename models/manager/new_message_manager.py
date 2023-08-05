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
        self._message = message

        self.message_data: Optional[MessagePublicChat] = None
        self.user: Union[Creator, Admin, Member, None] = None
        self.group: Optional[Group] = None

        self._message_serializer: Optional[MessagePublicChatSerializer] = None
        self._user_serializer: Union[CreatorSerializer, AdminSerializer, MemberSerializer, None] = None
        self._group_serializer: Optional[GroupSerializer] = None
        self._group_member_role_serializer: Optional[GroupMemberRoleSerializer] = None

        self.message_data_dict: Optional[dict] = None
        self.group_dict: Optional[dict] = None
        self.user_dict: Optional[dict] = None
        self.group_member_role_dict: Optional[dict] = None

        self.name_col: Optional[str] = None

    @abstractmethod
    async def serialize(self) -> None:
        pass

    @abstractmethod
    async def add_to_db(self):
        pass

    async def _serialize_process(self) -> None:
        print(Fore.LIGHTYELLOW_EX + f'{self._serialize_process.__name__} in class {self.__class__.__name__}')

        self.message_data_dict = await self._message_serializer.to_json(
            self.message_data)  # return dict (don't use) with message data and save json
        self.user_dict = await self._user_serializer.to_json(
            self.user)  # return dict (don't use) with member data and save json
        self.group_dict = await self._group_serializer.to_json(
            self.group)  # return dict (don't use) with group data and save json
        self.group_member_role_dict = await self._group_member_role_serializer.to_json(
            self.message_data)  # return dict (don't use) with group_id, user_id and role and save json


class NewMessageFromCreatorManager(NewMessageManager):
    def __init__(self, message: Message):
        super().__init__(message)
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.message_data = MessagePublicChat(self._message)
        self.user = Creator(self._message)
        self.group = Group(self._message)

    async def serialize(self) -> None:
        print(Fore.LIGHTYELLOW_EX + f'{self.serialize.__name__} in class {self.__class__.__name__}')

        self._message_serializer = MessagePublicChatSerializer()
        self._user_serializer = CreatorSerializer()
        self._group_serializer = GroupSerializer()
        self._group_member_role_serializer = GroupMemberRoleSerializer()

        await self._serialize_process()

    async def add_to_db(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.serialize.__name__} in class {self.__class__.__name__}')



class NewMessageFromAdminManager(NewMessageManager):
    def __init__(self, message: Message):
        super().__init__(message)
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.message_data = MessagePublicChat(self._message)
        self.user = Admin(self._message)
        self.group = Group(self._message)

    async def serialize(self) -> None:
        print(Fore.LIGHTYELLOW_EX + f'{self.serialize.__name__} in class {self.__class__.__name__}')

        self._message_serializer = MessagePublicChatSerializer()
        self._user_serializer = AdminSerializer()
        self._group_serializer = GroupSerializer()
        self._group_member_role_serializer = GroupMemberRoleSerializer()

        await self._serialize_process()

    async def add_to_db(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.serialize.__name__} in class {self.__class__.__name__}')


class NewMessageFromMemberManager(NewMessageManager):
    def __init__(self, message: Message):
        super().__init__(message)
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.message_data = MessagePublicChat(self._message)
        self.user = Member(self._message)
        self.group = Group(self._message)

    async def serialize(self) -> None:
        print(Fore.LIGHTYELLOW_EX + f'{self.serialize.__name__} in class {self.__class__.__name__}')

        self._message_serializer = MessagePublicChatSerializer()
        self._user_serializer = MemberSerializer()
        self._group_serializer = GroupSerializer()
        self._group_member_role_serializer = GroupMemberRoleSerializer()

        await self._serialize_process()

    async def add_to_db(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.serialize.__name__} in class {self.__class__.__name__}')
