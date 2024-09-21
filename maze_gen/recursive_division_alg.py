from common import WIDTH, HEIGHT
from common import grid_to_list
from common import list_to_grid
from common import SEARCH_DIRECTION

import matplotlib.pyplot as plt
import random


class RecursiveDivisionGen:
    def __init__(self):
        self.connect = [[False for _ in range(WIDTH * HEIGHT)] for __ in range(WIDTH * HEIGHT)]

    def gen(self):
        self.recursive_division(0, WIDTH - 1, 0, HEIGHT - 1)
        self.maze_render()
        self.refresh()

    def recursive_division(self, x_min: int, x_max: int, y_min: int, y_max: int):
        if x_max < x_min or y_max < y_min:
            return
        width_length = x_max - x_min + 1
        height_length = y_max - y_min + 1
        if width_length == 1 and height_length == 1:
            return
        if width_length == 1:
            for j in range(y_min, y_max):
                ind1 = grid_to_list(x_min, j)
                ind2 = grid_to_list(x_min, j + 1)
                self.connect[ind1][ind2] = True
                self.connect[ind2][ind1] = True
            return
        if height_length == 1:
            for i in range(x_min, x_max):
                ind1 = grid_to_list(i, y_min)
                ind2 = grid_to_list(i + 1, y_min)
                self.connect[ind1][ind2] = True
                self.connect[ind2][ind1] = True
            return
        if width_length > height_length:
            x_choose = random.randint(x_min, x_max - 1)
            y_choose = random.randint(y_min, y_max)
            ind1 = grid_to_list(x_choose, y_choose)
            ind2 = grid_to_list(x_choose + 1, y_choose)
            self.connect[ind1][ind2] = True
            self.connect[ind2][ind1] = True

            self.recursive_division(x_min, x_choose, y_min, y_max)
            self.recursive_division(x_choose + 1, x_max, y_min, y_max)
        else:
            x_choose = random.randint(x_min, x_max)
            y_choose = random.randint(y_min, y_max - 1)
            ind1 = grid_to_list(x_choose, y_choose)
            ind2 = grid_to_list(x_choose, y_choose + 1)
            self.connect[ind1][ind2] = True
            self.connect[ind2][ind1] = True

            self.recursive_division(x_min, x_max, y_min, y_choose)
            self.recursive_division(x_min, x_max, y_choose + 1, y_max)

    def maze_render(self):
        fig, ax = plt.subplots(figsize=(6, 6))
        plt.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0)

        for j in range(HEIGHT):
            for i in range(WIDTH):
                ind1 = grid_to_list(i, j)
                ind2 = grid_to_list(i, j + 1)
                ind3 = grid_to_list(i + 1, j)
                if i + 1 < WIDTH:
                    if not self.connect[ind1][ind3]:
                        ax.plot([i + 1, i + 1], [j, j + 1], c='black')
                if j + 1 < HEIGHT:
                    if not self.connect[ind1][ind2]:
                        ax.plot([i, i + 1], [j + 1, j + 1], c='black')

        ax.plot([0, 0], [0, HEIGHT], c='black')
        ax.plot([WIDTH, WIDTH], [0, HEIGHT], c='black')

        ax.plot([0, WIDTH], [0, 0], c='black')
        ax.plot([0, WIDTH], [HEIGHT, HEIGHT], c='black')

        ax.set_aspect(1)
        plt.xlim((-0.5, WIDTH + 0.5))
        plt.ylim((-0.5, HEIGHT + 0.5))
        plt.axis('off')
        plt.show()

    def refresh(self):
        self.connect.clear()
        self.connect = [[False for _ in range(WIDTH * HEIGHT)] for __ in range(WIDTH * HEIGHT)]


