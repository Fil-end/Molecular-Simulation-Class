import numpy as np
import matplotlib.pyplot as plt

L = 30
Iteration_num = 1000

def get_initial_grid(L:int = L) -> np.asarray:
    grid = np.zeros((L,L,L))
    for _ in range(L**3):
        x = np.random.randint(L)
        y = np.random.randint(L)
        z = np.random.randint(L)
            
        if int(grid[x][y][z]) == 0:
            grid[x][y][z] = 1
        
        if np.sum(grid) == L**3 / 2:
            break
    return grid

total_energy_list = []
for chk_idx in range(Iteration_num):
    print(f"-----------{chk_idx}------------")
    total_energy = 0
    initial_grid = get_initial_grid()

    for x in range(L):
        for y in range(L):
            for z in range(L):
                if initial_grid[x][y][z] == 1:
                    neighbour_list = []
                    if x == 0:
                        neighbour_list.extend([(1, y, z),(L-1, y, z)])
                    elif x == L - 1:
                        neighbour_list.extend([(L-2, y, z), (0,y,z)])
                    else:
                        neighbour_list.extend([(x-1, y, z), (x+1,y,z)])
                    
                    if y == 0:
                        neighbour_list.extend([(x,1,z), (x, L-1,z)])
                    elif y == L - 1:
                        neighbour_list.extend([(x,L-2,z), (x,0,z)])
                    else:
                        neighbour_list.extend([(x,y-1,z), (x,y+1,z)])
                    
                    if z == 0:
                        neighbour_list.extend([(x,y,1), (x, y,L-1)])
                    elif z == L - 1:
                        neighbour_list.extend([(x,y,L-2), (x,y,0)])
                    else:
                        neighbour_list.extend([(x,y,z-1), (x, y,z+1)])

                    for neighbour in neighbour_list:
                        if initial_grid[neighbour[0]][neighbour[1]][neighbour[2]] == 1:
                            total_energy += 0.3
    
    total_energy = total_energy / 2            
    total_energy_list.append(total_energy)

iter_num_list = list(range(Iteration_num))
plt.figure(figsize=(15, 15), dpi=100)
plt.scatter(iter_num_list, total_energy_list, c='blue', s=100)
plt.xlabel("Iter", fontdict={'size': 16})
plt.ylabel("Total Energy/(eV)", fontdict={'size': 16})
plt.title("Total interation = 1000", fontdict={'size': 20})
plt.savefig("./total_energy.png", bbox_inches='tight')

average_energy = np.average(total_energy_list)
energy_rmse = np.sqrt(np.sum((total_energy_list - average_energy) ** 2) / Iteration_num)
print(f"The average energy is {average_energy}")
print(f"The RMSE is {energy_rmse}")