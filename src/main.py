import numpy as np

# initialising necessary global variables
starting_grid = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
                          [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                          [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
                          [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, -1],
                          [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                          [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                          [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                          [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                          [2, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])  # -1 is the starting, 2 is the goal
grid_rows, grid_columns = starting_grid.shape


class Node:
    def __init__(self, row, column, parent, operator, moves):
        self.row = row
        self.column = column
        self.parent = parent
        self.operator = operator
        self.moves = moves


def create_node(row, column, parent, operator, moves):
    return Node(row, column, parent, operator, moves)


def expand_node(node, visited):
    expanded_nodes = [create_node(move_up(node.row, node.column, visited), node.column, node, "Up", node.moves + 1),
                      create_node(node.row, move_left(node.row, node.column, visited), node, "Left", node.moves + 1),
                      create_node(node.row, move_right(node.row, node.column, visited), node, "Right", node.moves + 1),
                      create_node(move_down(node.row, node.column, visited), node.column, node, "Down", node.moves + 1)]
    expanded_nodes = [node for node in expanded_nodes if node.row is not None and node.column is not None]
    return expanded_nodes


def isVisited(row, column, visited):
    for i in visited:  # checking if node is already visited or not
        if i.row == row and i.column == column:
            return True
    return False


def move_left(row, column, visited):
    if column != 0 and starting_grid[row][column - 1] in [1, 2] and not isVisited(row, column - 1, visited):
        return column - 1
    return None


def move_right(row, column, visited):
    if column != grid_columns - 1 and starting_grid[row][column + 1] in [1, 2]\
            and not isVisited(row, column + 1, visited):
        return column + 1
    return None


def move_up(row, column, visited):
    if row != 0 and starting_grid[row - 1][column] in [1, 2] and not isVisited(row - 1, column, visited):
        return row - 1
    return None


def move_down(row, column, visited):
    if row != grid_rows - 1 and starting_grid[row + 1][column] in [1, 2] and not isVisited(row + 1, column, visited):
        return row + 1
    return None

def dfs(starting_row, starting_column, goal_row, goal_column):
    startNode = create_node(starting_row, starting_column, None, None, 0)
    nodes = [startNode]
    visited = []
    cost = 0
    while nodes:
        node = nodes.pop(0)
        if node.row == goal_row and node.column == goal_column:
            return cost, node
        visited.append(node)
        expanded_nodes = expand_node(node, visited)
        cost += len(expanded_nodes)
        expanded_nodes.extend(nodes)
        nodes = expanded_nodes
    return -1, None


def main():
    # initialising starting coordinates and goal coordinates
    starting_row, starting_column = np.where(starting_grid == -1)  # -1 indicates starting point
    starting_row, starting_column = int(starting_row), int(starting_column)
    goal_row, goal_column = np.where(starting_grid == 2)  # 2 indicates goal point
    goal_row, goal_column = int(goal_row), int(goal_column)

    # applying algorithms and displaying output
    cost1, result1 = dfs(starting_row, starting_column, goal_row, goal_column)
    if result1 is None:
        print("No solution found using DFS.")
    else:
        print('Algorithm used = "DFS" , ', end='')
        print("No of path steps = ", result1.moves, ", No of searching steps = ", cost1)


if __name__ == "__main__":
    main()
