WIDTH = 20
HEIGHT = 20

SEARCH_DIRECTION = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def list_to_grid(ind: int):
    x: int = ind % WIDTH
    y: int = (ind - x) // WIDTH
    return x, y


def grid_to_list(x: int, y: int):
    ind = x + y * WIDTH
    return ind
