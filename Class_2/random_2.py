import math
import numpy as np
import matplotlib.pyplot as plt

L = 100

iter_num = 20
x_list = list(range(iter_num))
y_list = []
linear_list = []
cube = np.zeros((L,L,L))
for I in range(iter_num):
    for _ in range(L**3):
        x = np.random.randint(L)
        y = np.random.randint(L)
        z = np.random.randint(L)
        
        if int(cube[x][y][z]) == 0:
            cube[x][y][z] = 1
    
    y_list.append(-np.log(1 - np.sum(cube)/L**3))
    linear_list.append((1 - np.sum(cube)/L**3)/np.exp(-I))

plt.figure(figsize=(15, 15), dpi=100)
plt.scatter(x_list, y_list, c='blue', s=100)
plt.xlabel("I", fontdict={'size': 16})
plt.ylabel("Empty_ratio", fontdict={'size': 16})
# plt.ylabel("Empty_ratio/I", fontdict={'size': 16})
# plt.title("Linear plot", fontdict={'size': 20})

plt.savefig("./empty_ratio.png", bbox_inches='tight')