from astar import astar
from plot import plot_path
from smooth_plot import plot_smooth_path


grid = [[0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]]

start = (0, 0)
end = (4, 4)

path = astar(grid, start, end)
# plot_path(grid, path, start, end)
plot_smooth_path(grid, path, start, end)
