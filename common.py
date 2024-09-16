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


class MyStack:
    def __init__(self):
        self.data: list[int] = []

    def empty(self) -> bool:
        return len(self.data) == 0

    def push(self, element: int):
        self.data.append(element)

    def top(self) -> int:
        if not self.empty():
            return self.data[-1]
        return -1

    def pop(self):
        self.data.pop()

    def clear(self):
        self.data.clear()
