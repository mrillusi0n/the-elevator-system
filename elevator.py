class Elevator:
    def __init__(self):
        self.requests = []
        self.active_buttons = [False for _ in range(10)]
        self.stops = [False for _ in range(10)]
        # self.max_weight = 1170
        self.current_floor = 0
        self.direction = None

    def add_request(self, floor_num):
        self.requests.append(floor_num)
    
    def next_stop(self):
        # TODO: Determine the next stop
        pass

    def move(self):
        # TODO: Get the next stop and move the lift.
        # It has to increment `current_floor` one at a time,
        # and have a delay so that another request can be added.

        pass

    def press_button(floor_num):
        self.active_buttons[floor_num] = not self.active_buttons[floor_num]
           
    
