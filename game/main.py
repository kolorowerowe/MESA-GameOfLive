from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer

from GameModel import GameModel


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "r": 0.5}
    if agent.is_alive:
        portrayal["Color"] = "red"
    else:
        portrayal["Color"] = "grey"
        portrayal["r"] = 0.2
    return portrayal


if __name__ == '__main__':
    print('Game of live is starting ...')

    grid = CanvasGrid(agent_portrayal, 50, 50, 500, 500)

    chart = ChartModule([{"Label": "Alive", "Color": "Black"}])

    server = ModularServer(GameModel, [grid, chart], "Game of Live model",  {"width": 50, "height": 50, "probability": 0.3})
    server.port = 8521
    server.launch()
