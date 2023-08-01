from aiogram import Router
from filters.chat_type_filter import ChatTypeFilter
from filters.user_role_filter import UserRoleFilter
from aiogram.types import Message
from colorama import init, Fore

router = Router()
router.message.filter(ChatTypeFilter(chat_type=['group', 'supergroup']))
init(autoreset=True)


@router.message(UserRoleFilter('member'))
async def on_new_message_group_supergroup(message: Message):
    print(Fore.BLUE + 'on_new_message_group_supergroup FROM MEMBER')
    pass


@router.message(UserRoleFilter('admin'))
async def on_new_message_group_supergroup(message: Message):
    print(Fore.BLUE + 'on_new_message_group_supergroup FROM ADMIN')
    pass


@router.message(UserRoleFilter('creator'))
async def on_new_message_group_supergroup(message: Message):
    print(Fore.BLUE + 'on_new_message_group_supergroup FROM CREATOR')
    pass
