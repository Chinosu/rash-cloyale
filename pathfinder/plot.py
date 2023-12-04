import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


def path(grid, path, start, end):
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

def smooth_path(grid, path, start, end):
    grid_array = np.array(grid)
    fig, ax = plt.subplots()
    ax.imshow(grid_array, cmap='Greys')

    # Plot start and end
    ax.scatter(start[1], start[0], marker="o", color="blue", label="Start")
    ax.scatter(end[1], end[0], marker="o", color="red", label="End")

    if path:
        path_array = np.array(path)

        # Interpolate to create a smoother path
        x, y = path_array[:,1], path_array[:,0]
        t = range(len(path_array))
        interp_i = interp1d(t, x, kind='cubic')
        interp_j = interp1d(t, y, kind='cubic')

        t_new = np.linspace(0, len(path_array) - 1, num=100)
        x_new = interp_i(t_new)
        y_new = interp_j(t_new)

        ax.plot(x_new, y_new, color="green", label="Smooth Path")

    ax.grid(which="major", color="black", linestyle='-', linewidth=2)
    ax.set_xticks(np.arange(-0.5, len(grid[0]), 1))
    ax.set_yticks(np.arange(-0.5, len(grid), 1))

    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.legend()

    plt.show()
