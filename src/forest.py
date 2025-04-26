import numpy as np
from utils.visualize import display_binary_matrix, display_coloured_matrix, get_cmap
from collections import deque

class Forest:
    def __init__(self, n : int = 10, p : float = 0.1, diagnal : bool = False):
        self.n = n # Making an nxn grid
        self.p = p # prob of the cell being open
        self.diagnal = diagnal # if True, the diagnal cells are also considered connected

        self.grid = None
        self.random_grid = np.random.uniform(0, 1, (self.n, self.n))
        self.makegrid()

        self.groups = None
        self.visited = np.zeros((self.n, self.n))
        self.makegroups()
        

    def makegrid(self):
        self.grid = np.where(self.random_grid < self.p, 1, 0)
        self.visited = np.where(self.grid == 1, 1, 0)

    def printgrid(self, file_name=None):
        display_binary_matrix(self.grid, file_name)
    
    def dfs(self, i : int, j : int, group : list):
        if i < 0 or i >= self.n or j < 0 or j >= self.n or self.visited[i][j] == 1:
            return

        self.visited[i][j] = 1

        if self.grid[i][j] == 0:
            group.append((i, j))

            self.dfs(i + 1, j, group)
            self.dfs(i - 1, j, group)
            self.dfs(i, j + 1, group)
            self.dfs(i, j - 1, group)
    
    def bfs(self, i, j, group):
        queue = deque()

        queue.append((i,j))
        self.visited[i][j] = 1
        group.append((i,j))

        if not self.diagnal:
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        else:
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


        while queue:
            cn = queue.popleft()
            # print("Current node: %d" % cn)
            
            for direction in directions:
                ni = cn[0] + direction[0]
                nj = cn[1] + direction[1]

                if ni < 0 or ni >= self.n or nj < 0 or nj >= self.n:
                    continue

                if self.visited[ni][nj] == 1:
                    continue

                if self.grid[ni][nj] == 0:
                    queue.append((ni, nj))
                    self.visited[ni][nj] = 1
                    group.append((ni, nj))

        return group
    

    def makegroups(self):
        self.visited = np.zeros((self.n, self.n))
        groups = []

        # Find connected components using BFS        

        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 0 and self.visited[i][j] == 0:
                    group = []
                    self.bfs(i, j, group)
                    groups.append(group)
        
        self.groups = groups

    def _debug_printgroups(self):
        for i, group in enumerate(self.groups):
            print(f"Group {i}: {len(group)}")
            print(f"Group {i}: {group}")


    def printgroups(self, file_name=None):
        cmap = get_cmap(len(self.groups), name='hsv')
        matrix = np.zeros((self.n, self.n))
        for i, group in enumerate(self.groups):
            for cell in group:
                matrix[cell[0]][cell[1]] = i + 1
        display_coloured_matrix(matrix, file_name)

if __name__ == "__main__":
    n = 20
    forest = Forest(n, 0.5, False)
    forest.printgrid(f"grid_{n}x{n}.png")
    forest.printgroups(f"coloured_grid_{n}x{n}.png")
    # forest._debug_printgroups()
