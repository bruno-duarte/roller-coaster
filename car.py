from queue import Queue
from time import sleep
import threading


class Car(threading.Thread):

    trips = 0

    def __init__(self, id, C, passengers, Tm, mutex):
        self.id = id
        self.seats = Queue(C)
        self.passengers = passengers
        self.Tm = Tm
        self.mutex = mutex
        threading.Thread.__init__(self)

    def run(self):
        get_passenger = True
        left_the_queue = 0
        while True:
            if not self.passengers.empty():
                if get_passenger:
                    with self.mutex:
                        left_the_queue += 1
                        passenger = self.passengers.get()
                if not self.seats.full():
                    with self.mutex:
                        sleep(1)
                        self.seats.put(passenger)
                    print(f'Passenger {passenger.id} boarded')
                    if left_the_queue % 4 == 0:
                        get_passenger = False
                else:
                    with self.mutex:
                        print(f'Car {self.id} is running')
                        sleep(self.Tm)
                        print(f'Car {self.id} has fineshed running')
                        Car.trips += 1
                    while not self.seats.empty():
                        sleep(1)
                        passenger = self.seats.get()
                        self.seats.task_done()
                        print(f'Passenger {passenger.id} got off the car')
                    get_passenger = True
            elif Car.trips == 2:
                with self.mutex:
                    Car.trips += 1
                    print(f'Car {self.id} is running')
                    sleep(self.Tm)
                    print(f'Car {self.id} has fineshed running')
                while True:
                    if not self.seats.empty():
                        sleep(1)
                        passenger = self.seats.get()
                        self.seats.task_done()
                        print(f'Passenger {passenger.id} got off the car')
                    else:
                        get_passenger = True
                        break
            elif Car.trips > 2:
                break
