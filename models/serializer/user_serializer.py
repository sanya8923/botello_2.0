from serializer import Serializer
from models.objects.user import User, Member, MiddleMember, NewMember, Admin, Creator
from other import print_name_method
from typing import Optional


class UserSerializer(Serializer):
    def __init__(self, user: User):
        super().__init__(user)
        self.user_id: int = user.id
        self.username: str = user.username
        self.user_first_name: str = user.first_name
        self.user_last_name: str = user.last_name
        self.user_status: Optional[str] = None

    @print_name_method
    async def to_json(self):  # TODO: add method
        pass

    @print_name_method
    async def from_json(self):  # TODO: add method
        pass


class MemberSerializer(UserSerializer):
    def __init__(self, member: Member):
        super().__init__(member)


class MiddleMemberSerializer(MemberSerializer):
    def __init__(self, member: MiddleMember):
        super().__init__(member)


class NewMemberSerializer(MemberSerializer):
    def __init__(self, member: NewMember):
        super().__init__(member)


class AdminSerializer(UserSerializer):
    def __init__(self, admin: Admin):
        super().__init__(admin)


class CreatorSerializer(UserSerializer):
    def __init__(self, creator: Creator):
        super().__init__(creator)

