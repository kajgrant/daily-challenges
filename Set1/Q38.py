class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, height):

    arr = []
    
    def helper(root, height, arr):
        if root == None or height < 0:
            return arr

        if height == 0:
            arr.append(root.value)
    
        height-=1
        helper(root.left, height, arr)
        helper(root.right, height, arr)

    helper(root, height-1, arr)

    return arr
    


#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print valuesAtHeight(a, 3)
# [4, 5, 7]