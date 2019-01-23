class PassiveBlock:
    @property
    def is_action(self):
        return False
class ActionBlock:
    @property
    def is_action(self):
        return True
