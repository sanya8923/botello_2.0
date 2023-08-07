from bot import bot
from dp import dp
import logging
import asyncio
from handlers import on_new_message_group
from colorama import init, Fore


async def main():
    init(autoreset=True)
    logging.basicConfig(level=logging.INFO, format=Fore.WHITE + '%(message)s')

    dp.include_routers(on_new_message_group.router)kfd

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=['message', 'callback_query', 'chat_member', 'my_chat_member'])

if __name__ == '__main__':
    asyncio.run(main())

