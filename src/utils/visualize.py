import matplotlib.pyplot as plt
import numpy as np

def display_binary_matrix(matrix, file_name=None):
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

    if file_name:
        plt.savefig(file_name, dpi=300)

    plt.show()

# Taken from https://stackoverflow.com/a/25628397
def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.get_cmap(name, n)

def display_coloured_matrix(matrix, file_name=None):
    matrix = np.array(matrix)

    fig, ax = plt.subplots()
    cmap = get_cmap(matrix.shape[0]*matrix.shape[1])
    ax.imshow(matrix, cmap=cmap, interpolation='none')

    # Add grid lines
    ax.set_xticks(np.arange(-0.5, matrix.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-0.5, matrix.shape[0], 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=1)

    # Turn off axis labels
    ax.set_xticks([])
    ax.set_yticks([])

    if file_name:
        plt.savefig(file_name, dpi=300)

    plt.show()