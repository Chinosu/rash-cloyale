import matplotlib.pyplot as plt
import numpy as np
from astar import astar


def plot_path(grid, path, start, end):
    # Convert grid to numpy array for easier plotting
    grid_array = np.array(grid)
    
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the grid
    ax.imshow(grid_array, cmap='Greys')

    # Plot the start and end points
    ax.scatter(start[1], start[0], marker="o", color="blue", label="Start")
    ax.scatter(end[1], end[0], marker="o", color="red", label="End")

    # Plot the path
    if path is not None:
        path_array = np.array(path)
        ax.plot(path_array[:, 1], path_array[:, 0], color="green", label="Path")

    # Set grid
    ax.grid(which="major", color="black", linestyle='-', linewidth=2)
    ax.set_xticks(np.arange(-0.5, len(grid[0]), 1))
    ax.set_yticks(np.arange(-0.5, len(grid), 1))
    
    # Set labels and show legend
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.legend()

    # Show the plot
    plt.show()

