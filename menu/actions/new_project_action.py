from menu.actions.base_action import BaseAction


class NewProjectAction(BaseAction):
    def __init__(self, parent):
        super().__init__(parent, 'New Project...', self.my_action_handler)

    def my_action_handler(self):
        print('pass')
