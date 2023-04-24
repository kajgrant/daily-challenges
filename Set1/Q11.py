class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
  

    while root_node != None:
        if root_node.value > k:
            ceil = root_node
            root_node = root_node.left
        elif root_node.value < k:
            floor = root_node
            root_node = root_node.right  
        else:
            floor = root_node
            ceil = root_node
    
    return floor.value, ceil.value


root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print findCeilingFloor(root, 5)
# (4, 6)

#        8
#      4   12
#    2  6 10 14