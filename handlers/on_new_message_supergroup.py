from aiogram import Router
from colorama import init, Fore
from aiogram.types import Message
from filters.user_role_filter import UserRoleFilter
from filters.chat_type_filter import ChatTypeFilter
from models.objects.update import MessagePublicChat
from models.objects.user import MiddleMember, NewMember, Admin, Creator
from models.objects.chat import Group

router = Router()
router.message(ChatTypeFilter('group'))
init(autoreset=True)


@router.message(UserRoleFilter(user_role='creator'))
async def on_new_message_from_creator_group(message: Message):
    print(Fore.BLUE + 'on_new_message_from_creator_group')


@router.message(UserRoleFilter(user_role='administrator'))
async def on_new_message_from_admin_group(message: Message):
    print(Fore.BLUE + 'on_new_message_from_admin_group')


@router.message(UserRoleFilter(user_role='member'))
async def on_new_message_from_member_group(message: Message):
    print(Fore.BLUE + 'on_new_message_from_member_group')
