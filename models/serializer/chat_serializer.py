from serializer import Serializer
from models.objects.chat import Chat, PublicChat, PrivateChat
from other import print_name_method


class ChatSerializer(Serializer):
    def __init__(self, chat: Chat):
        super().__init__(chat)
        self.chat = chat
        self.id = chat.id


class PrivateChatSerializer(ChatSerializer):
    def __init__(self, chat: PrivateChat):
        super().__init__(chat)


class PublicChatSerializer(ChatSerializer):
    def __init__(self, chat: PublicChat):
        super().__init__(chat)
        self.username = chat.username
        self.title = chat.title

    @print_name_method
    async def to_json(self):
        pass

    @print_name_method
    async def from_json(self):
        pass
