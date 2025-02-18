from core.controller_registry import ControllerRegistry
import logging

class CommandExecutor:

    @staticmethod
    def execute(command):
        controller = ControllerRegistry.get_controller(command)
        logging.info(f"Полученный контроллер: {controller}")
        if controller:
            controller.execute(command)
        else:
            logging.info(f"Не найден контроллер для команды: {command.__class__.__name__}")