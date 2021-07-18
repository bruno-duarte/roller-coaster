
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
USAGE_TIME = 'Cars usage time is {}%'


def show_message(message, id=None, time=None):
    if id: print(message.format(id))
    elif time: print(message.format(time))
    else: print(message)
