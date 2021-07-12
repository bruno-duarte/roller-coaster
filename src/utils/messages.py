
CAR_IS_RUNNING = 'Car {} is running'
CAR_HAS_FINESHED_RUNNING = 'Car {} has fineshed running'

PASSENGER_BOARDED = 'Passenger {} boarded'
PASSENGER_GOT_OFF = 'Passenger {} got off the car'
PASSENGER_ARRIVAL = 'Passenger {} just arrived'

INVALID_OPTION = 'Opção inválida!'
        

def show_message(message, id=None):
    if id: print(message.format(id))
    else: print(message)
