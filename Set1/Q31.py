class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enqueue(self, val):
        self.s1.append(val)

    def dequeue(self):
        
        if len(self.s1) == 0 and len(self.s2) == 0:
            print "Q is Empty"
            return
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
        else:
            return self.s2.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print q.dequeue()
print q.dequeue()
print q.dequeue()
# 1 2 3