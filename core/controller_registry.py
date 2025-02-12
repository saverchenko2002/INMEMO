class ControllerRegistry:
    _registry = {}

    @classmethod
    def register(cls, command_class, controller_instance):
        cls._registry[command_class] = controller_instance

    @classmethod
    def get_controller(cls, command):
        for base_class, controller in cls._registry.items():
            return controller
