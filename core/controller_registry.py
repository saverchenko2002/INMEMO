class ControllerRegistry:
    _registry = {}

    @classmethod
    def register(cls, command_class, controller_instance):
        cls._registry[command_class] = controller_instance

    @classmethod
    def get_controller(cls, command):
        print(type(command))

        for command_class, controller in cls._registry.items():
            if issubclass(command.__class__, command_class):
                return controller

        print(f"Не найден контроллер для команды: {type(command).__name__}")
        return None

