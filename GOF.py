import pygame
import numpy as np
import time

# global variables
refresh_time = 0.05
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GRAY = (50, 50, 50)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
BLOCK_SIZE = 10
rows = WINDOW_HEIGHT // BLOCK_SIZE
columns = rows

# pygame template
pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
pygame.display.set_caption('Game of Life')
SCREEN.fill(GRAY)


# Random 2D array
def make_2d_array(rws, clmns):
    array = np.random.randint(2, size=(rws, clmns))
    return array


# Draw the Grid
def draw_grid(block_size, matrix):
    for x in range(0, WINDOW_WIDTH, block_size):
        for y in range(0, WINDOW_HEIGHT, block_size):
            index = matrix[x // block_size][y // block_size]
            rect_colors = [GRAY, WHITE]
            rect_color = rect_colors[index]
            rect = pygame.Rect(y, x, block_size - 2, block_size - 2)
            pygame.draw.rect(SCREEN, rect_color, rect)


# Next Generation Grid
def next_gen(parent_grid):
    child_grid = parent_grid.copy()
    for i in range(rows):
        for j in range(columns):
            if parent_grid[i][j] == 1:
                counter = -1
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if parent_grid[(i + x + rows) % rows][(j + y + rows) % rows] == 1:
                            counter = counter + 1
                if counter > 3 or counter < 2:
                    child_grid[i][j] = 0
                else:
                    child_grid[i][j] = 1
            else:
                counter = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if parent_grid[(i + x + rows) % rows][(j + y + rows) % rows] == 1:
                            counter = counter + 1
                        if counter == 3:
                            child_grid[i][j] = 1
                        else:
                            child_grid[i][j] = 0
    return child_grid


# Initial Conditions
grid = make_2d_array(rows, columns)


# Game Loop
running = True
while running:
    time.sleep(refresh_time)
    draw_grid(BLOCK_SIZE, grid)
    nextgen = next_gen(grid)
    grid = nextgen.copy()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
