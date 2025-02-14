import copy


class StateManager:
    def __init__(self):
        self._state = {}

    def get_snapshot(self):
        return self._state.copy()

    def get_state_value(self, key):
        value = self._state.get(key)
        if isinstance(value, (dict, list, set)):
            return copy.deepcopy(value)
        return value

    def set_state_value(self, key, value):
        if isinstance(value, (dict, list, set)):
            self._state[key] = copy.deepcopy(value)
        else:
            self._state[key] = value
