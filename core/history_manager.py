class HistoryManager:
    def __init__(self):
        self._history = []
        self._redo_stack = []

    def add_to_history(self, state):
        self._history.append(state.copy())
        self._redo_stack.clear()

    def undo(self, state):
        self._redo_stack.append(state.copy())
        return self._history.pop()

    def redo(self, state):
        self._history.append(state.copy())
        return self._redo_stack.pop()
