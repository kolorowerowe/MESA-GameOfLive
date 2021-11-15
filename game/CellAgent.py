from mesa import Agent


class CellAgent(Agent):
    is_alive = False

    def __init__(self, unique_id, model, is_alive):
        super().__init__(unique_id, model)
        self.is_alive = is_alive

    def check_aliveness(self):
        alive_to_alive_rule = [4, 5, 6, 7]
        dead_to_alive_rule = [3]

        cellmates = self.model.grid.neighbor_iter(self.pos, moore=True)
        living_neighbours_count = len(list(filter(lambda x: x.is_alive, cellmates)))

        if self.is_alive:
            if living_neighbours_count not in alive_to_alive_rule:
                self.is_alive = False
        else:
            if living_neighbours_count in dead_to_alive_rule:
                self.is_alive = True

    def step(self):
        self.check_aliveness()
