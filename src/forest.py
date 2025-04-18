import numpy as np
from utils.visualize import display_binary_matrix, display_coloured_matrix, get_cmap

class Forest:
    def __init__(self, n : int = 10, p : float = 0.1):
        self.n = n # Making an nxn grid
        self.p = p # prob of the cell being open

        self.grid = None
        self.random_grid = np.random.uniform(0, 1, (self.n, self.n))
        self.makegrid()

        self.groups = None
        self.makegroups()
        

    def makegrid(self):
        self.grid = np.where(self.random_grid < self.p, 1, 0)

    def printgrid(self):
        display_binary_matrix(self.grid)
    
    def dfs(self, i : int, j : int, visited : np.ndarray, group : list):
        if i < 0 or i >= self.n or j < 0 or j >= self.n or visited[i][j] == 1:
            return

        visited[i][j] = 1

        if self.grid[i][j] == 0:
            group.append((i, j))

            self.dfs(i + 1, j, visited, group)
            self.dfs(i - 1, j, visited, group)
            self.dfs(i, j + 1, visited, group)
            self.dfs(i, j - 1, visited, group)
    

    def makegroups(self):
        visited = np.zeros((self.n, self.n))
        groups = []

        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 0 and visited[i][j] == 0:
                    group = []
                    self.dfs(i, j, visited, group)
                    groups.append(group)
        
        self.groups = groups

    def _debug_printgroups(self):
        for i, group in enumerate(self.groups):
            print(f"Group {i}: {len(group)}")
            print(f"Group {i}: {group}")


    def printgroups(self):
        cmap = get_cmap(len(self.groups), name='hsv')
        matrix = np.zeros((self.n, self.n))
        for i, group in enumerate(self.groups):
            for cell in group:
                matrix[cell[0]][cell[1]] = i + 1
        display_coloured_matrix(matrix)


