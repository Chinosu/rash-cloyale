"""
Console app to develop pathfinding algorithm.
"""


class Node:
    # Initialize a node with its position, parent, g, h, and f values
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

def heuristic(node, goal):
    # Use octile distance as a heuristic for a grid with diagonal movement
    dx = abs(node.position[0] - goal.position[0])
    dy = abs(node.position[1] - goal.position[1])
    return max(dx, dy) + (2**0.5 - 1) * min(dx, dy)

def astar(grid, start, end):
    # Initialize start and end nodes
    start_node = Node(start, None)
    end_node = Node(end, None)

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        # Find the node in open_list with the lowest f score
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)
        closed_list.append(current_node)

        # If we have reached the goal, reconstruct the path and return it
        if current_node.position == end_node.position:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Generate children nodes (all adjacent squares including diagonals)
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Check within range and not an obstacle
            if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid)-1]) - 1) or node_position[1] < 0:
                continue
            if grid[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node and append to children
            new_node = Node(node_position, current_node)
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is in the closed list
            if child in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = heuristic(child, end_node)
            child.f = child.g + child.h

            # Child is already in the open list
            if any(child.position == open_node.position and child.g > open_node.g for open_node in open_list):
                continue

            # Add the child to the open list
            open_list.append(child)

    return None  # No path found
