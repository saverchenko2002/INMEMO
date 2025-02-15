from core.controller_registry import ControllerRegistry


class CommandExecutor:

    @staticmethod
    def execute(command):
        controller = ControllerRegistry.get_controller(command)
        print(f"Полученный контроллер: {controller}")
        print('вытащил для тебя контроллер')
        print(command is None, 'коМАНА ИЗ НАН ??? ')
        if controller:
            controller.execute(command)
        else:
            print(f"Не найден контроллер для команды: {command.__class__.__name__}")