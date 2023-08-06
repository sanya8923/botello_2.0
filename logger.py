import logging
import inspect
import time
from colorama import Fore, init
from contextlib import suppress
import copy

init(autoreset=True)


class MyLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(Fore.BLUE + '%(asctime)s: %(message)s')

        # Добавляем обработчик для вывода логов на консоль
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def log_class_info(self, function):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = function(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time

            stack = inspect.stack()
            frame = stack[2]

            class_name_line = frame[4][0].split('=')
            pattern = frame[3].strip()

            with suppress(IndexError):  # TODO: это неправильно. Переделай
                class_name = copy.deepcopy(class_name_line[1])
                if pattern != 'wrapper' and pattern != '__init__':
                    print(Fore.BLUE + f'Class {class_name[:-1]}. Speed: {execution_time:.6f} sec')
            return result

        return wrapper

    def log_method_info(self, function):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = function(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time

            stack = inspect.stack()
            method_name = stack[1].function
            print(Fore.BLUE + f'{method_name.ljust(20)} {execution_time:.8f} sec')

            return result

        return wrapper
