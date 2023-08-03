from aiogram import Router
from colorama import init, Fore
from aiogram.types import Message

from filters.user_role_filter import UserRoleFilter
from filters.chat_type_filter import ChatTypeFilter

from models.objects.user import MiddleMember, NewMember, Admin, Creator
from models.serializer.user_serializer import MiddleMemberSerializer, NewMemberSerializer, AdminSerializer, CreatorSerializer

from models.objects.chat import Group
from models.serializer.chat_serializer import GroupSerializer

from models.objects.update import MessagePublicChat
from models.serializer.update_serializer import MessagePublicChatSerializer

router = Router()
router.message(ChatTypeFilter('group'))
init(autoreset=True)


@router.message(UserRoleFilter(user_role='creator'))
async def on_new_message_from_creator_group(message: Message):
    print(Fore.BLUE + 'on_new_message_from_creator_group')
    message_data = MessagePublicChat(message)
    creator = Creator(message)
    group = Group(message)
    await MessagePublicChatSerializer(message_data).to_json()  # return dict with message data (analog for json)
    await CreatorSerializer(creator).to_json()  # return dict with member data (analog for json)
    await GroupSerializer(group).to_json()  # return dict with group data (analog for json)


@router.message(UserRoleFilter(user_role='administrator'))
async def on_new_message_from_admin_group(message: Message):
    print(Fore.BLUE + 'on_new_message_from_admin_group')


@router.message(UserRoleFilter(user_role='member'))
async def on_new_message_from_member_group(message: Message):
    print(Fore.BLUE + 'on_new_message_from_member_group')
