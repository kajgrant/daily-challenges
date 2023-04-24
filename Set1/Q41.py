from collections import deque

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      n = q.popleft()
      result += n.val
      if n.left:
        q.append(n.left)
      if n.right:
        q.append(n.right)

    return result


def reconstruct(preorder, inorder):

    def array_to_tree(left, right):
        nonlocal preorder_index
        if left > right: return None

        root_value = preorder[preorder_index]
        root = Node(root_value)

        preorder_index += 1

        root.left = array_to_tree(left, inorder_index_map[root_value]-1)
        root.right = array_to_tree(inorder_index_map[root_value]+1, right)

        return root
    
    preorder_index = 0

    inorder_index_map = {}
    for index, value in enumerate(inorder):
        inorder_index_map[value] = index

    return array_to_tree(0, len(preorder)-1)

tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
print tree
# abcdefg