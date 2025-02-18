import logging

class ControllerRegistry:
    _registry = {}

    @classmethod
    def register(cls, command_class, controller_instance):
        cls._registry[command_class] = controller_instance

    @classmethod
    def get_controller(cls, command):

        for command_class, controller in cls._registry.items():
            if issubclass(command.__class__, command_class):
                return controller

        logging.info(f"Не найден контроллер для команды: {type(command).__name__}")
        return None

