class TV():
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = True
    def show_status(self):
        return self.is_on

