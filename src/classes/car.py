
from queue import Queue
from time import sleep
import threading

from ..utils.messages import (
    show_message, 
    CAR_IS_RUNNING, 
    CAR_HAS_FINESHED_RUNNING
)

class Car(threading.Thread):

    rides = 0

    def __init__(self, id, C, passengers, Tm, Te, m, mutex):
        self.id = id
        self.seats = Queue(C)
        self.passengers = passengers
        self.Tm = Tm
        self.Te = Te
        self.m = m
        self.mutex = mutex
        threading.Thread.__init__(self)

    def run(self):
        while True:
            while not self.seats.full():
                if not self.passengers.empty():
                    passenger = self.passengers.get()
                    passenger.board(self.Te)
                    self.seats.put(passenger)
                if self.stop_car():
                    break
            with self.mutex:
                if self.seats.full():
                    Car.rides += 1
                    self.move()
            self.unload_passengers()
            if self.stop_car():
                break

    def unload_passengers(self):
        while not self.seats.empty():
            passenger = self.seats.get()
            passenger.unboard(self.Te)
            self.seats.task_done()

    def move(self):
        show_message(CAR_IS_RUNNING, self.id)
        sleep(self.Tm)
        show_message(CAR_HAS_FINESHED_RUNNING, self.id)
        
    def stop_car(self):
        return Car.rides == 13 and self.m == 1 or \
            Car.rides == 23 and self.m == 2 or \
            Car.rides == 37 and self.m == 3
