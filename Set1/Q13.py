import collections

class MaxStack:
  def __init__(self):
    self.stack = collections.deque()
    self.max_stack = collections.deque()

  def push(self, val):
    self.stack.append(val)
    if not self.max_stack:
        self.max_stack.append(val)
    elif self.max_stack and val >+ self.max_stack[-1]:
        self.max_stack.append(val)

  def pop(self):
    ele = self.stack.pop()
    if self.max_stack and ele == self.max_stack[-1]:
        self.max_stack.pop()

  def max(self):
    if self.max_stack:
        return self.max_stack[-1]
    else:
        return None

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print s.max()
# 3
s.pop()
s.pop()
print s.max()
# 2