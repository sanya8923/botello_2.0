from models.serializer.serializer import Serializer
from models.objects.update import UpdateData, MessageData, MessagePublicChat, MessagePrivateChat, Callback
from colorama import init, Fore

init(autoreset=True)


class UpdateSerializer(Serializer):
    def __init__(self, update: UpdateData):
        super().__init__(update)
        print(Fore.BLUE + f'{self.__class__.__name__}')

    async def to_json(self):  # abstract method
        pass

    async def from_json(self):  # abstract method
        pass


class MessageDataSerializer(UpdateSerializer):
    def __init__(self, message: MessageData):
        super().__init__(message)
        print(Fore.BLUE + f'{self.__class__.__name__}')

        self.id: int = message.id
        self.message_text: str = message.text
        self.from_user: int = message.from_user.id
        self.from_chat: int = message.from_chat.id
        self.file: str = 'jsons/message.json'

    async def to_json(self):
        print(Fore.LIGHTYELLOW_EX + f'{self.to_json.__name__} in class {self.__class__.__name__}')

        data = {
            'id': self.id,
            'text': self.message_text,
            'from_user': self.from_user,
            'from_chat': self.from_chat
        }

        await self.add_to_json(self.file, data)

        return data

    async def from_json(self):  # TODO: add method
        pass


class MessagePrivateChatSerializer(MessageDataSerializer):
    def __init__(self, message: MessagePrivateChat):
        super().__init__(message)
        print(Fore.BLUE + f'{self.__class__.__name__}')


class MessagePublicChatSerializer(MessageDataSerializer):
    def __init__(self, message: MessagePublicChat):
        super().__init__(message)
        print(Fore.BLUE + f'{self.__class__.__name__}')


class CallbackSerializer(UpdateSerializer):
    def __init__(self, callback: Callback):
        super().__init__(callback)
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.callback_data: str = callback.callback_data
