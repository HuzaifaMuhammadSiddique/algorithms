from util import Node, QueueFrontier
from copy import deepcopy

def main():
    grid = [
    [0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 0]
            ]
    
    result = shortest_path(grid)
    
    print(f"Number of actions: {result[0]}")
    print(f"Path taken: {result[1]}")
    


def shortest_path(grid):  # grid is a 2D-list
    
    goal_coordinates = (len(grid) - 1, len(grid[0]) - 1)
    goal_value = 0
    start_value = grid[0][0]
    initial_node = Node(value=start_value, parent=None, action=None, no_of_actions=0,path=[], coordinate=(0,0), parent_coordinate=None)

    
    actions = ["right", "left", "up", "down"]
    
    frontier = QueueFrontier()
    
    explored = set()
    
    frontier.add(initial_node)
    
    while True:
        if frontier.is_empty():
            raise Exception("Empty! No solution.")
        
        node = frontier.remove()
        
        
        if node.coordinate == goal_coordinates and node.value == goal_value:
            return (node.no_of_actions, node.path)
        
        
        explored.add(node)
        
        for action in actions:
            try:
                new_node = movement(node, grid, action)
                if new_node.value == 0 and not frontier.contains(new_node.coordinate) and new_node not in explored:
                    frontier.add(new_node)
            except Exception:
                pass
            
        
    
# returns the child node    
def movement(node, grid, action):
    current_position = node.coordinate
    if action.lower() == "right":
        current_position = (current_position[0], current_position[1] + 1)
    elif action.lower() == "left":
        current_position = (current_position[0], current_position[1] - 1)
    elif action.lower() == "up":
        current_position = (current_position[0] - 1, current_position[1])
    elif action.lower() == "down":
        current_position = (current_position[0] + 1, current_position[1])
    else:
        raise Exception("Invalid Action")
    
    if current_position[0] < 0 or current_position[1] < 0:
        raise Exception
    
    child_node = deepcopy(node)
    child_node.value = grid[current_position[0]][current_position[1]]
    child_node.parent = node
    child_node.action = action
    child_node.no_of_actions += 1
    child_node.path.append(action)
    child_node.coordinate = current_position
    child_node.parent_coordinate = node.coordinate
    
    
    return child_node
    
    
if __name__ == "__main__":
    main()
    
    
