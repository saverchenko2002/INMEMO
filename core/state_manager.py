class StateManager:
    def __init__(self):
        self._state = {}

    def get_snapshot(self):
        return self._state.copy()

    def get_state_value(self, key):
        return self._state[key]

    def set_state_value(self, key, value):
        self._state[key] = value
