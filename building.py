from elevator import Elevator
from floor import Floor

# create the elevator
eli = Elevator()

# create floors
floors = [Floor(i, eli) for i in range(10)]
