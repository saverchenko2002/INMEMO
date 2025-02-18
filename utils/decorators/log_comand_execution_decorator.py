import logging
from functools import wraps


def log_command_execution(func):
    @wraps(func)
    def wrapper(self, command, *args, **kwargs):
        logging.info(f"Обработка команды {command.__class__.__name__}")
        return func(self, command, *args, **kwargs)
    return wrapper
