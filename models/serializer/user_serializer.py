from models.serializer.serializer import Serializer
from models.objects.user import User, Member, MiddleMember, NewMember, Admin, Creator
from typing import Optional
from colorama import init, Fore

init(autoreset=True)


class UserSerializer(Serializer):
    def __init__(self, user: User):
        super().__init__(user)
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.user_id: int = user.id
        self.username: str = user.username
        self.user_first_name: str = user.first_name
        self.user_last_name: str = user.last_name
        self.user_status: Optional[str] = None

    async def to_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')
        pass

    async def from_json(self):  # TODO: add method
        print(Fore.LIGHTYELLOW_EX + f'{self.from_json.__name__} in class {self.__class__.__name__}')
        pass


class MemberSerializer(UserSerializer):
    def __init__(self, member: Member):
        super().__init__(member)
        print(Fore.BLUE + f'{self.__class__.__name__}')


class MiddleMemberSerializer(MemberSerializer):
    def __init__(self, member: MiddleMember):
        super().__init__(member)
        print(Fore.BLUE + f'{self.__class__.__name__}')


class NewMemberSerializer(MemberSerializer):
    def __init__(self, member: NewMember):
        super().__init__(member)
        print(Fore.BLUE + f'{self.__class__.__name__}')


class AdminSerializer(UserSerializer):
    def __init__(self, admin: Admin):
        super().__init__(admin)
        print(Fore.BLUE + f'{self.__class__.__name__}')


class CreatorSerializer(UserSerializer):
    def __init__(self, creator: Creator):
        super().__init__(creator)
        print(Fore.BLUE + f'{self.__class__.__name__}')

