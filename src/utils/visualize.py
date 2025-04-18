import matplotlib.pyplot as plt
import numpy as np

def display_binary_matrix(matrix):
    matrix = np.array(matrix)

    fig, ax = plt.subplots()
    ax.imshow(matrix, cmap='Greys', interpolation='none')

    # Add grid lines
    ax.set_xticks(np.arange(-0.5, matrix.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-0.5, matrix.shape[0], 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=1)

    # Turn off axis labels
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()

# Example usage
binary_matrix = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]

# display_binary_matrix(binary_matrix)
