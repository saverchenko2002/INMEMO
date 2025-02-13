from core.state_manager import StateManager
from core.history_manager import HistoryManager
from core.event_bus import EventBus


class AppStateService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.state_manager = StateManager()
            cls._instance.history_manager = HistoryManager()
            cls._instance.event_bus = EventBus()
        return cls._instance

    def get_state(self, key):
        return self.state_manager.get_state_value(key)

    def set_state(self, key, value):
        self.state_manager.set_state_value(key, value)
        print('отработал стейт')
        self.history_manager.add_to_history(self.state_manager.get_snapshot())
        print('отработала история')
        self.event_bus.notify(key, value)

    def undo(self):
        self.history_manager.undo(self.state_manager.get_snapshot())

    def redo(self):
        self.history_manager.redo(self.state_manager.get_snapshot())

    def subscribe(self, key, component):
        self.event_bus.subscribe(key, component)
