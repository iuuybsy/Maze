from common import WIDTH, HEIGHT
from common import grid_to_list

import matplotlib.pyplot as plt
import random


class SidWinderGen:
    def __init__(self):
        self.connect = [[False for _ in range(WIDTH * HEIGHT)] for __ in range(WIDTH * HEIGHT)]

    def gen(self):
        for j in range(HEIGHT - 1):
            last_run = 0
            for i in range(WIDTH - 1):
                guess = random.randint(0, 1)
                if guess == 0:
                    ind1 = grid_to_list(i, j)
                    ind2 = grid_to_list(i + 1, j)
                    self.connect[ind1][ind2] = True
                else:
                    rand_ind = random.randint(last_run, i)
                    last_run = i + 1
                    ind1 = grid_to_list(rand_ind, j)
                    ind2 = grid_to_list(rand_ind, j + 1)
                    self.connect[ind1][ind2] = True
            rand_ind = random.randint(last_run, WIDTH - 1)
            ind1 = grid_to_list(rand_ind, j)
            ind2 = grid_to_list(rand_ind, j + 1)
            self.connect[ind1][ind2] = True
        for i in range(WIDTH - 1):
            ind1 = grid_to_list(i, HEIGHT - 1)
            ind2 = grid_to_list(i + 1, HEIGHT - 1)
            self.connect[ind1][ind2] = True

        self.maze_render()
        self.refresh()

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



