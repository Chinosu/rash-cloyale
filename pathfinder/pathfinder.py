from astar import astar
import plot
import parse


class Pathfinder:
    def __init__(self, grid_str) -> None:
        self.grid = parse.grid(grid_str)
    
    def update_grid(self, grid_str):
        self.grid = parse.grid(grid_str)

    def path(self, start, end):
        path = astar(self.grid, start, end)

        self.last_start = start
        self.last_end = end
        self.last_path = path
        return path

    def print_grid(self):
        raise NotImplemented()
    
    def print_path(self, smooth=True, path=None, start=None, end=None):
        if path is None:
            path = self.last_path
        if start is None:
            start = self.last_start
        if end is None:
            end = self.last_end

        if smooth:
            plot.smooth_path(self.grid, path, start, end)
        else:
            plot.path(self.grid, path, start, end)


#  ------ DEMO ------ #
def demo():
    map = """
    0  0  0  0  1
    1  1  0  0  0
    0  0  0  1  0
    0  1  1  1  0
    0  0  0  0  0
    """
    pathfinder = Pathfinder(map)
    path = pathfinder.path((0, 0), (4, 4))
    pathfinder.print_path()
