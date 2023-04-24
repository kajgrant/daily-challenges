class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

def is_bst(root):
    def helper(root, min_val, max_val):
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        helper(root.left, min_val, root.val)
        helper(root.right, root.val, max_val)
    helper(root, -float('inf'), float('inf'))


a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print is_bst(a)

#    5
#   / \
#  3   7
# / \ /
#1  4 6
