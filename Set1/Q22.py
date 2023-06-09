def intersection(a, b):
    node = a
    while node:
        node.seen = True
        node = node.next
    
    node = b
    while node:
        try:
            if node.seen:
                return node
        except:
            node = node.next

    return None

class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
  def prettyPrint(self):
    c = self
    while c:
      print c.val,
      c = c.next

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
c.prettyPrint()
# 3 4