import numpy as np

L = 20
cube = np.zeros((L,L))

for _ in range(1):
    for _ in range(int(L**2/4)):
        x = np.random.randint(L)
        y = np.random.randint(L)
        z = np.random.randint(L)
        
        if int(cube[x][y]) == 0:
            cube[x][y] = 1
    
def percolate(grid, start):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] == 1 or visited[r][c]:
            return
        visited[r][c] = True
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    dfs(start[0], start[1])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and visited[r][c]:
                grid[r][c] = 2

    return grid

# Example usage
cube[0][0] = 0
start = (0, 0)

result = percolate(cube, start)
for row in result:
    print(row)