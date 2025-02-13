from core.state_manager import StateManager


class ReactiveStateManager(StateManager):
    def __init__(self):
        super().__init__()
        self.observers = {}

    def subscribe(self, key, observer):
        pass
