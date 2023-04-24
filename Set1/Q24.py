class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def removeConsecutiveSumTo0(node):

    dummy = Node(0)
    dummy.next = node
    prefix = 0
    d = {0:dummy}
    while node:
        prefix += node.value
        d[prefix] = node
        node = node.next
    
    node = dummy
    prefix = 0
    while node:
        prefix += node.value
        node.next = d[prefix].next
        node = node.next
    
    return dummy.next




node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
  print node.value,
  node = node.next
# 10