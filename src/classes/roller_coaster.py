from queue import Queue
from time import sleep as passenger_arrival
from random import randint as arrival_time
import time

import threading

from .passenger import Passenger
from .car import Car
import src.utils.globals as globals
from ..utils.messages import (
    show_message,
    PASSENGER_ARRIVAL
)


class RollerCoaster:

    def __init__(self, n, m, C, Te, Tm, Tp):
        self.n = n
        self.m = m
        self.C = C
        self.Te = Te
        self.Tm = Tm
        self.Tp = Tp
        self.queue = Queue(n)
        self.cars = []

    def run(self):
        globals.start_time = time.perf_counter()
        cp_threading = threading.Thread(target=self.create_passengers)
        cc_threading = threading.Thread(target=self.create_cars)
        cp_threading.start()
        cc_threading.start()
        cp_threading.join()
        cc_threading.join()

    def create_passengers(self):
        for id in range(self.n):
            tp = arrival_time(1, self.Tp)
            passenger_arrival(tp)
            passenger = Passenger(id + 1, self.Te)
            globals.passengers_time[passenger.id] = [time.perf_counter()]
            show_message(PASSENGER_ARRIVAL, passenger.id)
            self.queue.put(passenger)

    def create_cars(self):
        for id in range(self.m):
            self.cars.append(
                Car(id + 1, self.C, self.queue, self.Tm, self.Te, self.m))
        for car in self.cars:
            car.start()
