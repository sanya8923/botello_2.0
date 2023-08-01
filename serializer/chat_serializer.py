from serializer import Serializer
from models.chat import Chat, PublicChat
from other import name_method


class ChatSerializer(Serializer):
    def __init__(self, chat: Chat):
        super().__init__(chat)
        self.chat = chat
        self.id = chat.id


class PublicChatSerializer(ChatSerializer):
    def __init__(self, chat: PublicChat):
        super().__init__(chat)
        self.username = chat.username
        self.title = chat.title

    @name_method
    async def to_json(self):
        pass

    @name_method
    async def from_json(self):
        pass
