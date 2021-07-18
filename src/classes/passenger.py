from time import sleep
import threading
from ..utils.messages import (
    show_message, 
    PASSENGER_BOARDED, 
    PASSENGER_GOT_OFF, 
    PASSENGER_LEFT_ROLLER_COASTER
)


class Passenger(threading.Thread):

    def __init__(self, id, Te):
        self.id = id
        self.Te = Te
        threading.Thread.__init__(self)

    def run(self):
        self.unboard(self.Te)
        sleep(self.Te)
        show_message(PASSENGER_LEFT_ROLLER_COASTER, self.id)
        
    def board(self, Te):
        sleep(Te)
        show_message(PASSENGER_BOARDED, self.id)

    def unboard(self, Te):
        sleep(Te)
        show_message(PASSENGER_GOT_OFF, self.id)
