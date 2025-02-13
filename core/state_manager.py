class StateManager:
    def __init__(self):
        self.state = {}

    def get_state(self):
        print('getstate  ebana')
        print(self.state)
        return self.state

    def set_state(self, key, value):
        self.state[key] = value
        print(self.state)
        print('state ebana')
