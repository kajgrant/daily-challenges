class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

def is_palindrome(node):
    char_arr = []
    iter = node
    i = 0

    ref_node = node

    if not node:
        return True

    while iter.next:
        ref_node = iter
        iter = iter.next

    if node.val != iter.val:
        return False

    ref_node.next = None

    return is_palindrome(node.next)


node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

print is_palindrome(node)
# True