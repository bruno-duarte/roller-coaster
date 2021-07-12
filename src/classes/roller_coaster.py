from queue import Queue
from time import sleep as passenger_arrival
from random import randint as arrival_time

import threading

from .passenger import Passenger
from .car import Car
from ..utils.messages import (
    show_message,
    PASSENGER_ARRIVAL
)

mutex = threading.Lock()


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

        for id in range(self.m):
            self.cars.append(
                Car(id + 1, self.C, self.queue, self.Tm, self.Te, self.m, mutex))

    def run(self):
        threading.Thread(target=self.manage_passenger).start()
        threading.Thread(target=self.manage_car).start()

    def manage_passenger(self):
        for id in range(self.n):
            time = arrival_time(1, self.Tp)
            passenger_arrival(time)
            passenger = Passenger(id + 1)
            show_message(PASSENGER_ARRIVAL, passenger.id)
            self.queue.put(passenger)

    def manage_car(self):
        for car in self.cars:
            car.start()
