from serializer import Serializer
from models.objects.chat import Chat, PublicChat, PrivateChat, Group, SuperGroup
from other import print_name_method


class ChatSerializer(Serializer):
    def __init__(self, chat: Chat):
        super().__init__(chat)
        self.chat = chat
        self.id = chat.id

    async def to_json(self):  # abstract method
        pass

    async def from_json(self):  # abstract method
        pass


class PrivateChatSerializer(ChatSerializer):
    @print_name_method
    def __init__(self, chat: PrivateChat):
        super().__init__(chat)

    @print_name_method
    async def to_json(self):  # TODO: add method
        pass

    @print_name_method
    async def from_json(self):  # TODO: add method
        pass


class PublicChatSerializer(ChatSerializer):
    @print_name_method
    def __init__(self, chat: PublicChat):
        super().__init__(chat)
        self.username = chat.username
        self.title = chat.title

    @print_name_method
    async def to_json(self):  # TODO: add method
        pass

    @print_name_method
    async def from_json(self):  # TODO: add method
        pass


class GroupSerializer(PublicChatSerializer):
    @print_name_method
    def __init__(self, chat: Group):
        super().__init__(chat)


class SuperGroupSerializer(PublicChatSerializer):
    def __init__(self, chat: SuperGroup):
        super().__init__(chat)

