from queue import Queue
from time import sleep
import threading
import time

from ..utils.report import show_report
from ..utils.messages import (
    show_message, 
    CAR_IS_RUNNING,
    CAR_HAS_FINESHED_RUNNING
)
import src.utils.globals as globals

monitor = threading.Lock()


class Car(threading.Thread):

    rides = 0
    stopped_cars = 0

    def __init__(self, id, C, passengers, Tm, Te, m):
        self.id = id
        self.seats = Queue(C)
        self.passengers = passengers
        self.Tm = Tm
        self.Te = Te
        self.m = m
        self.allow_boarding = True
        self.is_running = False
        threading.Thread.__init__(self)

    def run(self): 
        while True:
            with monitor:
                while not self.seats.full():
                    if not self.passengers.empty() and self.allow_boarding and not self.is_running:
                        passenger = self.passengers.get()
                        globals.passengers_time[passenger.id] += [time.perf_counter()]
                        passenger.board(self.Te)
                        self.seats.put(passenger)
                    if self.stop_car():
                        break
            if self.seats.full():
                if Car.rides == 0:
                    globals.running_start_time = time.perf_counter()
                Car.rides += 1
                self.move()
            self.unload_passengers()
            if self.stop_car():
                Car.stopped_cars += 1
                globals.finish_time = time.perf_counter()
                globals.total_time = round(globals.finish_time - globals.start_time, 2)
                if self.m == 1 and Car.stopped_cars == 1: 
                    show_report()
                elif self.m == 2 and Car.stopped_cars == 2: 
                    show_report()
                elif self.m == 3 and Car.stopped_cars == 3: 
                    show_report()
                break

    def unload_passengers(self):
        self.allow_boarding = False
        while not self.seats.empty():
            passenger = self.seats.get()
            passenger.start()
            passenger.join()
            self.seats.task_done()
        self.allow_boarding = True
        if self.stop_car():
            globals.running_finish_time = time.perf_counter()

    def move(self):
        self.is_running = True
        show_message(CAR_IS_RUNNING, self.id)
        sleep(self.Tm)
        show_message(CAR_HAS_FINESHED_RUNNING, self.id)
        self.is_running = False
        
    def stop_car(self):
        return Car.rides == 13 and self.m == 1 or \
            Car.rides == 23 and self.m == 2 or \
            Car.rides == 37 and self.m == 3
