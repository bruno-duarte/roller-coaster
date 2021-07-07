from time import sleep


class Passenger():

    def __init__(self, id):
        self.id = id

    def board(self, Te):
        sleep(Te)
        print(f'Passenger {self.id} boarded')

    def unboard(self, Te):
        sleep(Te)
        print(f'Passenger {self.id} got off the car')
