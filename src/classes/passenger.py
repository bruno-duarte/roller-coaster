from ..utils.messages import (
    show_message, 
    PASSENGER_BOARDED, 
    PASSENGER_GOT_OFF
)
from time import sleep


class Passenger():

    def __init__(self, id):
        self.id = id

    def board(self, Te):
        sleep(Te)
        show_message(PASSENGER_BOARDED, self.id)

    def unboard(self, Te):
        sleep(Te)
        show_message(PASSENGER_GOT_OFF, self.id)
