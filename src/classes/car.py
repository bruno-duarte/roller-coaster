from queue import Queue
from time import sleep
import threading


class Car(threading.Thread):

    trips = 0

    def __init__(self, id, C, passengers, Tm, Te, mutex):
        self.id = id
        self.seats = Queue(C)
        self.passengers = passengers
        self.Tm = Tm
        self.Te = Te
        self.mutex = mutex
        self.get_passenger = True
        threading.Thread.__init__(self)

    def run(self):
        left_the_queue = 0
        while True:
            if not self.passengers.empty():
                if self.get_passenger:
                    with self.mutex:
                        left_the_queue += 1
                        passenger = self.passengers.get()
                if not self.seats.full():
                    with self.mutex:
                        passenger.board(self.Te)
                        self.seats.put(passenger)
                    if left_the_queue % 4 == 0:
                        self.get_passenger = False
                else:
                    with self.mutex:
                        self.move()
                        Car.trips += 1
                    self.unload_passengers()
            elif Car.trips == 2:
                with self.mutex:
                    Car.trips += 1
                    self.move()
                self.unload_passengers()
            elif Car.trips > 2:
                break

    def unload_passengers(self):
        while not self.seats.empty():
            passenger = self.seats.get()
            passenger.unboard(self.Te)
            self.seats.task_done()
        self.get_passenger = True

    def move(self):
        print(f'Car {self.id} is running')
        sleep(self.Tm)
        print(f'Car {self.id} has fineshed running')
