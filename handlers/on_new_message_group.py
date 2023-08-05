from aiogram import Router
from colorama import init, Fore
from aiogram.types import Message

from filters.user_role_filter import UserRoleFilter
from filters.chat_type_filter import ChatTypeFilter
from models.manager.new_message_manager import NewMessageFromCreatorManager, NewMessageFromAdminManager, \
    NewMessageFromMemberManager


router = Router()
router.message(ChatTypeFilter('group'))
init(autoreset=True)


@router.message(UserRoleFilter(user_role='creator'))
async def on_new_message_from_creator_group(message: Message):

    manager = NewMessageFromCreatorManager(message)
    await manager.serialize()
    await manager.add_to_db()


@router.message(UserRoleFilter(user_role='administrator'))
async def on_new_message_from_admin_group(message: Message):

    manager = NewMessageFromAdminManager(message)
    await manager.serialize()


@router.message(UserRoleFilter(user_role='member'))
async def on_new_message_from_member_group(message: Message):

    manager = NewMessageFromMemberManager(message)
    await manager.serialize()

