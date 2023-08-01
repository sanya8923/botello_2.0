from typing import Callable
from colorama import init, Fore


async def print_name_method(func: Callable):
    init(autoreset=True)
    print(Fore.BLUE + f'{func.__name__}')
    return func
