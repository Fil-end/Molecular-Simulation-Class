import numpy as np
import matplotlib.pyplot as plt

x_rand = np.random.rand(5000)
y_rand = np.random.rand(5000)

plt.figure(figsize=(15, 15), dpi=100)
plt.scatter(x_rand, y_rand, c='blue', s=100)
plt.xlabel("X_rand", fontdict={'size': 16})
plt.ylabel("y_rand", fontdict={'size': 16})
plt.title("Random", fontdict={'size': 20})

plt.savefig("./rand.png", bbox_inches='tight')
