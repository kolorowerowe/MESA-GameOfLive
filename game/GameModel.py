from mesa import Model
from mesa.time import RandomActivation
from mesa.space import Grid
from mesa.datacollection import DataCollector
from CellAgent import CellAgent
from random import random


class GameModel(Model):

    description = "This is Conway's Game of Live model. Implemented by Dominik Kołodziej and Szymon Borowy"

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
        self.schedule.step()
        self.datacollector.collect(self)

    def count_alive(self):
        """
        Helper method to count trees in a given condition in a given model.
        """
        alive = len(list(filter(lambda a: a.is_alive, self.schedule.agents)))
        print(f'Alive: {alive}')
        return alive
