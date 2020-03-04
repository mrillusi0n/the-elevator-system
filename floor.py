class Floor:
    def __init__(self, number, elevator):
        self.number = number
        self.elevator = elevator

    def press_button(self):
        self.elevator.add_request(self.number)


