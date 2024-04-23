import numpy as np
import matplotlib.pyplot as plt

import time

L = 100
cube = np.zeros((L,L))
rows, cols = cube.shape[0], cube.shape[1]

for _ in range(L**2):
    x = np.random.randint(L)
    y = np.random.randint(L)

    if int(cube[x][y]) == 0:
        cube[x][y] = 1
    
    if np.sum(cube) == 5000:
        break
energy_list = []
s_t = time.time()
for _ in range(10000):
    energy = 0
    for row in range(rows):
        for col in range(row, cols):
            if cube[row][col] == 1:
                if row == 0 or row == rows-1:
                    energy += 0.15
                if col == 0 or col == cols -1:
                    energy += 0.15

                neighbour_list = []
                # [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                if row+1 <= rows-1:
                    neighbour_list.append((row+1, col))
                if row-1 >= 0:
                    neighbour_list.append((row-1, col))
                if col+1 <= cols-1:
                    neighbour_list.append((row, col+1))
                if col-1 >= 0:
                    neighbour_list.append((row, col-1))
                
                for neighbour in neighbour_list:
                    if cube[neighbour[0]][neighbour[1]] == 1:
                        energy += 0.35
    energy_list.append(energy)
print(f"The energy_list is {energy_list}")
print(f"The time consuming is {time.time() - s_t}")