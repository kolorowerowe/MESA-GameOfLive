from mesa import Model
from mesa.time import RandomActivation
from mesa.space import Grid
from mesa.datacollection import DataCollector
from CellAgent import CellAgent
from random import random
import time
import psutil


class GameModel(Model):

    description = "This is Conway's Game of Live model. Implemented by Dominik Kołodziej and Szymon Borowy"
    time_sum = 0
    cpu_sum = 0
    count = 0

    def __init__(self, width, height, probability):
        super().__init__()
        self.grid = Grid(width, height, True)
        self.schedule = RandomActivation(self)

        self.datacollector = DataCollector(
            {"Alive": lambda model: model.count_alive()})

        for i in range(width):
            for j in range(height):
                a = CellAgent(i * width + j, self, random() < probability)
                self.schedule.add(a)
                self.grid.place_agent(a, (i, j))

    def step(self):
        start = time.time()
        self.schedule.step()
        end = time.time()
        res = end - start

        self.time_sum += res
        self.count += 1
        # print(f'Mean time for step: {self.time_sum / self.count} with {self.count} steps')

        self.datacollector.collect(self)

        self.cpu_sum += psutil.cpu_percent()
        # print(f'Mean CPU usage: {self.cpu_sum / self.count} % with {self.count} steps')

    def count_alive(self):
        """
        Helper method to count trees in a given condition in a given model.
        """
        alive = len(list(filter(lambda a: a.is_alive, self.schedule.agents)))
        # print(f'Alive: {alive}')
        return alive
