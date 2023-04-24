class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def min_depth_bst(root):

    if root is None:
        return 0

    l = min_depth_bst(root.left)
    r = min_depth_bst(root.right)
    
    if root.left is None:
        return r + 1
    
    if root.right is None:
        return l + 1

    return min(l, r) 

    
n3 = Node(3, None, Node(4))
n2 = Node(2, Node(3))
n1 = Node(1, n2, n3)

#     1
#    / \
#   2   3
#        \
#         4
print(min_depth_bst(n1))
# 2
