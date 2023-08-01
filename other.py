from typing import Callable
from colorama import init, Fore


async def name_method(func: Callable):
    init(autoreset=True)
    print(Fore.BLUE + f'{func.__class__.__name__}.{func.__name__}')
    return func
