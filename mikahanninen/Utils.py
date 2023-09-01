class Utils:
    def __init__(self, impersonate:str = None):
        self.name = impersonate

    def return_name(self):
        return self.name or "Mika"