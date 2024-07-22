class Node():
    def __init__(self, value, parent, action, no_of_actions, path, coordinate, parent_coordinate):
        self.value = value   # 0 or 1
        self.parent = parent   # another node
        self.action = action   # "right", "left", "up", "down"
        self.no_of_actions = no_of_actions  # integer
        self.path = path  # array of actions
        self.coordinate = coordinate  # a tuple (i,j)
        self.parent_coordinate = parent_coordinate   # a tuple (i,j)
        
    
class QueueFrontier():
    def __init__(self):
        self.frontier = []
        
    def add(self, Node):
        self.frontier.append(Node)
        
    def contains(self, coordinate):
        return any(node.coordinate == coordinate for node in self.frontier)
    
    def is_empty(self):
        return len(self.frontier) == 0
        
    
    def remove(self):
        if self.is_empty():
            raise Exception("frontier is empty!")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
    
        
    
        
    