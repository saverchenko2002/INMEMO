class EventBus:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, key, component):
        if key not in self._subscribers:
            self._subscribers[key] = []
        self._subscribers[key].append(component)

    def notify(self, key, value):
        for component in self._subscribers.get(key, []):
            component.react_state_update(key, value)
