import numpy as np
import matplotlib.pyplot as plt

L = 10
Iterations = 50
STEPS = 50
cube = np.zeros((L,L))
    
def step(grid, start, steps:int = STEPS):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    current_r, current_c = start[0], start[1]

    def _displace(r, c):
        displacement_list = []
        # [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
        if r+1 <= rows:
            displacement_list.append((r+1, c))
        if r-1 >= 0:
            displacement_list.append((r-1, c))
        if c+1 <= cols:
            displacement_list.append((r, c+1))
        if c-1 >= 0:
            displacement_list.append((r, c-1))

        next_displacement = displacement_list[np.random.randint(len(displacement_list))]
        return next_displacement

    for _ in range(steps):
        next_displacement = _displace(current_r, current_c)
        current_r, current_c = next_displacement[0], next_displacement[1]
    
    final_r, final_c = current_r, current_c
    distance = np.linalg.norm(start - np.array([final_r, final_c]))
    return distance

# Example usage
start = np.array([0, 0])
distance_list = []

for _ in range(Iterations):
    distance = step(cube, start)
    distance_list.append(distance)

plt.plot(list(range(len(distance_list))), distance_list, c='blue')
plt.xlabel("iteration", fontdict={'size': 16})
plt.ylabel("displacement", fontdict={'size': 16})
plt.title("Displacement at steps = 50", fontdict={'size': 16})

plt.savefig("./displacement.png", bbox_inches='tight')