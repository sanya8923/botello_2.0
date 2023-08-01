from serializer import Serializer
from models.objects.update import Update, MessageData, MessagePublicChat, MessagePrivateChat, Callback
from other import print_name_method


class UpdateSerializer(Serializer):
    def __init__(self, update: Update):
        super().__init__(update)
        self.update: int = update.id

    async def to_json(self):  # abstract method
        pass

    async def from_json(self):  # abstract method
        pass


class MessageDataSerializer(UpdateSerializer):
    def __init__(self, message: MessageData):
        super().__init__(message)
        self.message_text: str = message.text
        self.from_user: int = message.from_user.id
        self.from_chat: int = message.from_chat.id

    async def to_json(self):  # abstract method
        pass

    async def from_json(self):  # abstract method
        pass


class MessagePrivateChatSerializer(MessageDataSerializer):
    @print_name_method
    def __init__(self, message: MessagePrivateChat):
        super().__init__(message)

    @print_name_method
    async def to_json(self):  # TODO: add method
        pass

    @print_name_method
    async def from_json(self):  # TODO: add method
        pass


class MessagePublicChatSerializer(MessageDataSerializer):
    def __init__(self, message: MessagePublicChat):
        super().__init__(message)

    @print_name_method
    async def to_json(self):  # TODO: add method
        pass

    @print_name_method
    async def from_json(self):  # TODO: add method
        pass


class CallbackSerializer(UpdateSerializer):
    def __init__(self, callback: Callback):
        super().__init__(callback)
        self.callback_data: str = callback.callback_data

    @print_name_method
    async def to_json(self):  # TODO: add method
        pass

    @print_name_method
    async def from_json(self):  # TODO: add method
        pass
