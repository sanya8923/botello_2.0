from models.serializer.serializer import Serializer
from typing import Optional
from models.objects.update import UpdateData, MessageData
import logger


class UpdateSerializer(Serializer):
    def __init__(self):
        super().__init__()

    @logger.MyLogger(name='log').log_method_info
    async def to_dict(self, update: UpdateData) -> dict:  # abstract method
        pass

    @logger.MyLogger(name='log').log_method_info
    async def from_json(self):  # abstract method
        pass

    @logger.MyLogger(name='log').log_method_info
    async def from_dict(self):  # abstract method
        pass


class MessageDataSerializer(UpdateSerializer):
    def __init__(self):
        super().__init__()

        self.id: Optional[int] = None
        self.message_text: Optional[str] = None
        self.from_user: Optional[int] = None
        self.from_chat: Optional[int] = None
        self.date = None
        self.file: str = 'jsons/message.json'

    @logger.MyLogger(name='log').log_method_info
    async def to_dict(self, update: MessageData) -> dict:
        self.id = update.id
        self.message_text = update.text
        self.from_user = update.from_user.id
        self.from_chat = update.from_chat.id
        self.date = update.date
        date = self.date.strftime("%Y-%m-%d %H:%M:%S %Z")

        data = {
            'id': self.id,
            'text': self.message_text,
            'from_user': self.from_user,
            'from_chat': self.from_chat,
            'date': date
        }
        return data

    @logger.MyLogger(name='log').log_method_info
    async def from_json(self):  # TODO: add method
        pass

    @logger.MyLogger(name='log').log_method_info
    async def from_dict(self):  # TODO: add method
        pass


class MessagePrivateChatSerializer(MessageDataSerializer):
    def __init__(self):
        super().__init__()


class MessagePublicChatSerializer(MessageDataSerializer):
    def __init__(self):
        super().__init__()


class CallbackSerializer(UpdateSerializer):
    def __init__(self):
        super().__init__()
        self.callback_data: Optional[str] = None
