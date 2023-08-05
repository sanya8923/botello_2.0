import logging
import inspect
import time
from colorama import init, Fore

init(autoreset=True)


class MyLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        # Создаем новый форматтер с нужным нам форматом
        formatter = logging.Formatter(Fore.YELLOW + '%(asctime)s: - %(levelname)s - %(message)s')

        # Добавляем обработчик для вывода логов на консоль
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def log_method_name(self):
        stack = inspect.stack()
        method_name = stack[1].function
        self.logger.info(f'{method_name} worked successful')  # TODO: do

    def log_with_execution_time(self, message, function):
        start_time = time.time()
        result = function(message)
        end_time = time.time()
        execution_time = end_time - start_time

        extra = {'elapsed': execution_time}
        self.logger.info(f'{message} {function.__name__}. Speed: {extra["elapsed"]}')
        return result

    def do_something(self):
        self.log_method_name()
        self.log_with_execution_time()
        # Ваша логика здесь