class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def count_unival_subtrees(root):
    count = [0]

    countSingle(root, count)

    return count[0]

def countSingle(root, count):
    if root is None:
        return True
    
    left = countSingle(root.left, count)
    right = countSingle(root.right, count)

    if not left or not right:
        return False

    if root.left and root.val != root.left.val:
        return False

    if root.right and root.val != root.right.val:
        return False

    count[0] += 1
    return True

a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print count_unival_subtrees(a)
# 5