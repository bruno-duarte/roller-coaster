def initialize():
    global start_time
    global finish_time
    global running_start_time
    global running_finish_time
    global total_time
    global passengers_time
    global cars_time
    global amount_of_cars

    start_time = None
    finish_time = None
    running_start_time = None
    running_finish_time = None
    total_time = None
    passengers_time = {}
    cars_time = {}
    cars_time[1] = 0
    cars_time[2] = 0
    cars_time[3] = 0
    amount_of_cars = None
