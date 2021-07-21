import src.utils.globals as globals

CAR_IS_RUNNING = 'Car {} is running'
CAR_HAS_FINESHED_RUNNING = 'Car {} has fineshed running'

PASSENGER_BOARDED = 'Passenger {} boarded'
PASSENGER_GOT_OFF = 'Passenger {} got off the car'
PASSENGER_ARRIVAL = 'Passenger {} just arrived'
PASSENGER_LEFT_ROLLER_COASTER = 'Passenger {} got of the roller coaster'

INVALID_OPTION = 'Invalid option!'

FINISH_TIME = 'Finished in {:.3f} second(s)'
MINIMUM_WAITING_TIME = 'Minimum passenger waiting time is {:.3f} second(s)'
MAXIMUM_WAITING_TIME = 'Maximum passenger waiting time is {:.3f} second(s)'
AVERAGE_WAITING_TIME = 'Average passenger waiting time is {:.3f} second(s)'
USAGE_TIME = 'Cars usage time is '


def show_message(message, id=None, time=None, percent=None):
    if id: 
        print(message.format(id))
    elif time: 
        print(message.format(time))
    elif percent: 
        if globals.amount_of_cars == 1:
            print(message + '[{:.2f}]'.format(percent[0]))
        elif globals.amount_of_cars == 2: 
            print(message + '[{:.2f}, {:.2f}]'.format(percent[0], percent[1]))
        else:
            print(message + '[{:.2f}, {:.2f}, {:.2f}]'.format(percent[0], percent[1], percent[2]))
    else: 
        print(message)
