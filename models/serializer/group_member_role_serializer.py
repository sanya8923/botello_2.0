from models.serializer.serializer import Serializer
from typing import Optional
from aiogram.types import Message
from bot import bot
from models.objects.chat import Group, SuperGroup
from models.objects.user import Admin, Member, Creator
from colorama import init, Fore

init(autoreset=True)


class GroupMemberRoleSerializer(Serializer):
    def __init__(self):
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.user_id: Optional[int] = None
        self.chat_id: Optional[int] = None
        self.role: Optional[str] = None
        self.file: str = 'jsons/group_member_role.json'

    async def to_json(self, message: Message):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        self.user_id = message.from_user.id
        self.chat_id = message.chat.id
        self.role = (await bot.get_chat_member(self.chat_id, self.user_id)).status

        data = {
            'user_id': self.user_id,
            'chat_id': self.chat_id,
            'role': self.role
        }

        await self.add_to_json(self.file, data)

        return data

    async def from_json(self):  # TODO: add method
        pass
