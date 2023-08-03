from models.serializer.serializer import Serializer
from models.objects.user import User, Member, MiddleMember, NewMember, Admin, Creator
from aiogram.types import Message
from typing import Optional
from colorama import init, Fore

init(autoreset=True)


class UserSerializer(Serializer):
    def __init__(self):
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.user_id: Optional[int] = None
        self.username: Optional[str] = None
        self.user_first_name: Optional[str] = None
        self.user_last_name: Optional[str] = None
        self.file: str = 'jsons/user.json'

    async def to_json(self, message: Message):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        self.user_id = message.from_user.id
        self.username = message.from_user.username
        self.user_first_name = message.from_user.first_name
        self.user_last_name = message.from_user.last_name

        data = {
            'id': self.user_id,
            'username': self.username,
            'first_name': self.user_first_name,
            'last_name': self.user_last_name
        }

        await self.add_to_json(self.file, data)

        return data

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass


class MemberSerializer(UserSerializer):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')


class AdminSerializer(UserSerializer):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')


class CreatorSerializer(UserSerializer):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')

