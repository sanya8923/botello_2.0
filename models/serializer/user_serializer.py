from models.serializer.serializer import Serializer
from models.objects.user import User
from typing import Optional
import logger


class UserSerializer(Serializer):
    def __init__(self):
        super().__init__()

        self.user_id: Optional[int] = None
        self.username: Optional[str] = None
        self.user_first_name: Optional[str] = None
        self.user_last_name: Optional[str] = None
        self.file: str = 'jsons/user.json'

    @logger.MyLogger(name='log').log_method_info
    async def to_dict(self, user: User) -> dict:

        self.user_id = user.id
        self.username = user.username
        self.user_first_name = user.first_name
        self.user_last_name = user.last_name

        data = {
            'id': self.user_id,
            'username': self.username,
            'first_name': self.user_first_name,
            'last_name': self.user_last_name
        }

        return data

    @logger.MyLogger(name='log').log_method_info
    async def from_json(self):  # TODO: add method
        pass

    @logger.MyLogger(name='log').log_method_info
    async def from_dict(self):  # TODO: add method
        pass


class MemberSerializer(UserSerializer):
    def __init__(self):
        super().__init__()


class AdminSerializer(UserSerializer):
    def __init__(self):
        super().__init__()


class CreatorSerializer(UserSerializer):
    def __init__(self):
        super().__init__()

