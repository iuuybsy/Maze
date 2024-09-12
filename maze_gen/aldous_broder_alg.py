from common import WIDTH, HEIGHT
from common import grid_to_list
from common import SEARCH_DIRECTION

import matplotlib.pyplot as plt
import random


class AldousBroderGen:
    def __init__(self):
        self.connect = [[False for _ in range(WIDTH * HEIGHT)] for __ in range(WIDTH * HEIGHT)]
        self.unvisited = [[True for _ in range(WIDTH)] for __ in range(HEIGHT)]
        self.total: int = WIDTH * HEIGHT

    def gen(self):
        x = random.randint(0, WIDTH - 1)
        y = random.randint(0, HEIGHT - 1)
        is_current_pos_unvisited: bool = True
        while self.total > 0:
            self.unvisited[x][y] = False
            if is_current_pos_unvisited:
                self.total -= 1
            ind = random.randint(0, len(SEARCH_DIRECTION) - 1)
            x_next = x + SEARCH_DIRECTION[ind][0]
            y_next = y + SEARCH_DIRECTION[ind][1]
            while not self.is_valid_cord(x_next, y_next):
                ind = random.randint(0, len(SEARCH_DIRECTION) - 1)
                x_next = x + SEARCH_DIRECTION[ind][0]
                y_next = y + SEARCH_DIRECTION[ind][1]
            if self.unvisited[x_next][y_next]:
                ind1 = grid_to_list(x, y)
                ind2 = grid_to_list(x_next, y_next)
                self.connect[ind1][ind2] = True
                self.connect[ind2][ind1] = True
                is_current_pos_unvisited = True
            else:
                is_current_pos_unvisited = False
            x, y = x_next, y_next

        self.maze_render()
        self.refresh()

    @classmethod
    def is_valid_cord(cls, x: int, y: int):
        return 0 <= x < WIDTH and 0 <= y < HEIGHT

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
        self.total = WIDTH * HEIGHT



