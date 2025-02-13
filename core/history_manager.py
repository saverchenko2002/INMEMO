class HistoryManager:
    def __init__(self):
        self.history = []
        self.redo_stack = []

    def add_to_history(self, state):
        self.history.append(state)
        self.redo_stack.clear()

    def undo(self, state):
        self.redo_stack.append(state.copy())
        return self.history.pop()

    def redo(self, state):
        self.history.append(state.copy())
        return self.redo_stack.pop()
