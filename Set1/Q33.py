class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

def merge(lists):
    return mergeKLists(lists)
    
def mergeKLists(lists):
    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount-interval, interval*2):
            lists[i] = merge2Lists(lists[i], lists[i + interval])
            interval *= 2
    return lists[0] if amount > 0 else None


def merge2Lists(l1, l2):
    head = point = Node(0)
    while l1 and l2:
        if l1.val <= l2.val:
            point.next = l1
            l1 = l1.next
        else:
            point.next = l2
            l2 = l1
            l1 = point.next.next
        point = point.next
    if not l1:
        point.next = l2
    else:
        point.next = l1
    return head.next


a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print merge([a, b])
# 123456