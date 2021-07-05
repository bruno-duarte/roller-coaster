from queue import Queue
from time import sleep
from random import randint as rand

import threading

from passenger import Passenger
from car import Car

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
            self.cars.append(Car(id + 1, self.C, self.queue, self.Tm, mutex))

    def run(self):
        threading.Thread(target=self.manage_passenger).start()
        threading.Thread(target=self.manage_car).start()

        # mp.join()
        # mc.join()

    def manage_passenger(self):
        for id in range(self.n):
            time = rand(1, 3)
            sleep(time)
            passenger = Passenger(id + 1)
            print(f'Passenger {passenger.id} just arrived')
            self.queue.put(passenger)

    def manage_car(self):
        for car in self.cars:
            car.start()


rc = RollerCoaster(12, 2, 4, 1, 10, 3)

rc.run()
