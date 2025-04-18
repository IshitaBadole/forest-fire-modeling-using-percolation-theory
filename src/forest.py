import numpy as np
from utils.visualize import display_binary_matrix

class Forest:
    def __init__(self, n : int = 10, p : float = 0.1):
        self.n = n # Making an nxn grid
        self.p = p # prob of the cell being open

        self.grid = None
        self.makegrid()

    def makegrid(self):
        self.grid = np.random.uniform(0, 1, (self.n, self.n))
        # [[random.uniform(0,1) for _ in range(self.n)] for _ in range(self.n) ]

        self.grid = np.where(self.grid < self.p, 1, 0)

    def printgrid(self):
        display_binary_matrix(self.grid)

