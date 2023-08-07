from models.serializer.serializer import Serializer
from typing import Optional
from bot import bot
from models.objects.update import MessageData


class GroupMemberRoleSerializer(Serializer):
    def __init__(self):
        super().__init__()

        self.user_id: Optional[int] = None
        self.chat_id: Optional[int] = None
        self.role: Optional[str] = None
        self.file: str = 'jsons/group_member_role.json'

    async def to_dict(self, update_data: MessageData) -> dict:

        self.user_id = update_data.from_user.id
        self.chat_id = update_data.from_chat.id
        self.role = (await bot.get_chat_member(self.chat_id, self.user_id)).status

        data = {
            'user_id': self.user_id,
            'chat_id': self.chat_id,
            'role': self.role
        }

        return data

    async def from_json(self):  # TODO: add method
        pass

    async def from_dict(self):  # TODO: add method
        pass
