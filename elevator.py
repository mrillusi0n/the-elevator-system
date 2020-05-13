# simulating the elevator system

NUM_FLOORS = 10

class Elevator:
    def __init__(self):
        self.requests = []
        self.active_buttons = [False for _ in range(NUM_FLOORS)]
        self.stops = [False for _ in range(NUM_FLOORS)]
        # self.max_weight = 1170
        self.current_floor = 0
        self.direction = None

    def add_request(self, floor_num):
        self.requests.append(floor_num)

    def next_stop(self):
        # TODO: Determine the next stop
        pass

    def move(self, floor_num):
        # TODO: Get the next stop and move the lift.
        # It has to increment `current_floor` one at a time,
        # and have a delay so that another request can be added.
        self.current_floor = floor_num
        del self.requests[0]

    def press_button(self, floor_num):
        self.active_buttons[floor_num] = not self.active_buttons[floor_num]
        self.add_request(floor_num)

    def get_active_buttons(self):
        return [i for i, status in enumerate(self.active_buttons) if status is True]

