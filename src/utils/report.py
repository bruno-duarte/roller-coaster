import src.utils.globals as globals
from .messages import *

def show_report():
    total = 0
    times = globals.passengers_time
    size = len(times)
    mintime = times[1][1] - times[1][0]
    maxtime = times[size][1] - times[size][0]
    for i in range(size):
        passenger_time = times[i + 1][1] - times[i + 1][0]
        total += passenger_time
        if passenger_time < mintime:
            mintime = passenger_time
        if passenger_time > maxtime:
            maxtime = passenger_time
    average_time = total / size
    running_total_time = globals.running_finish_time - globals.running_start_time
    usage_time_car1 = (globals.cars_time[1] * 10 / running_total_time) * 100
    usage_time_car2 = (globals.cars_time[2] * 10 / running_total_time) * 100
    usage_time_car3 = (globals.cars_time[3] * 10 / running_total_time) * 100
    
    print()
    print()
    print('REPORT')
    print('------------------------------------------------------')
    print()
    show_message(MINIMUM_WAITING_TIME, time=mintime)
    show_message(MAXIMUM_WAITING_TIME, time=maxtime)
    show_message(AVERAGE_WAITING_TIME, time=average_time)
    show_message(FINISH_TIME, time=globals.total_time)
    show_message(USAGE_TIME, percent=[usage_time_car1, usage_time_car2, usage_time_car3])
    print()
    print('------------------------------------------------------')

