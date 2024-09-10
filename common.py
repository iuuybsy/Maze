WIDTH = 20
HEIGHT = 20


def list_to_grid(ind: int):
    x = ind % WIDTH
    y = ind / (ind - x)
    return x, y


def grid_to_list(x: int, y: int):
    ind = x + y * WIDTH
    return ind
