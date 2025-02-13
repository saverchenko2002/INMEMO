from core.state_manager import StateManager
from core.history_manager import HistoryManager


class AppStateService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.state_manager = StateManager()
            cls._instance.history_manager = HistoryManager()
            cls._instance.subscribers = {}
        return cls._instance

    def get_state(self):
        return self.state_manager.get_state()

    def set_state(self, key, value):
        self.state_manager.set_state(key, value)
        self.history_manager.add_to_history(self.state_manager.get_state())
        print('все записали ёбана')
        self.notify_subscribers(key)
        print('всех оповестили ёбана')

    def undo(self):
        self.history_manager.undo(self.state_manager.get_state())

    def redo(self):
        self.history_manager.redo(self.state_manager.get_state())

    def subscribe(self, key, component):
        if key not in self.subscribers:
            self.subscribers[key] = []
        self.subscribers[key].append(component)
        print('отсос на подписке')
        print(self.subscribers)

    def notify_subscribers(self, key):
        print(self.subscribers)
        for component in self.subscribers[key]:
            print(key + 'ключ')
            print(type(component))
            component.react_state_update(key)
