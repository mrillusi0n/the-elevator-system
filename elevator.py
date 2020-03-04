class Elevator:
    def __init__(self, number):
        self.number = number
        self.requests = []
        self.active_buttons = [False for _ in range(10)]
        self.max_weight = 1170
        self.direction = None

    def add_request(self, floor_num):
        self.requests.append(floor_num)
    
    def next_stop
    
    
