from models.objects.object import Object
from colorama import init, Fore
from typing import Optional

init(autoreset=True)


class User(Object):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')
        self.id: Optional[int] = None
        self.username: Optional[str] = None
        self.first_name: Optional[str] = None
        self.last_name: Optional[str] = None
        self.new_member: bool = False  # TODO: когда будет готово подключение к БД добей сюда функцию


class Member(User):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')


class Admin(Member):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')


class Creator(Member):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')


class NotMember(User):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')


class Kicked(NotMember):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')


class Left(NotMember):
    def __init__(self):
        super().__init__()
        print(Fore.BLUE + f'{self.__class__.__name__}')
