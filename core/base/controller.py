from abc import ABC, abstractmethod


class Controller(ABC):
    def __init__(self):
        self.handlers = {}

    def execute(self, command):
        handler = self.handlers.get(command.__class__)
        print('достал хендлер по классу команды')
        if handler:
            handler(command)
        else:
            print(f"Нет обработчика для команды {command.__class__.__name__}")

    def add_handler(self, command_class, handler):
        self.handlers[command_class] = handler
