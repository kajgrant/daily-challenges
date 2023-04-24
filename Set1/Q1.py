#!/usr/bin/env python2.7

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):

    result = ListNode(-1) #Dummy result node
    result_tail = result #Result list (i.e Result->number1->number2->number3)
    carry = 0 #Overflow carry digit
            
    while l1 or l2: #Loop through both lists until we reach null
        val1  = (l1.val if l1 else 0) #l1 value, unless we have reached the end where we set to 0
        val2  = (l2.val if l2 else 0) #l2 value, unless we have reached the end where we set to 0
        sum = val1+val2+carry #sum of nodes and previous carry value
        carry, out = divmod(sum, 10) #set carry to sum mod10 and out to remainder of mod10 
                  
        result_tail.next = ListNode(out) #set node value to remainder of mod10
        result_tail = result_tail.next #go to next result node
        
        l1 = (l1.next if l1 else None) #go to next l1 node
        l2 = (l2.next if l2 else None) #go to next l2 node
            
    return result.next #return but ignore first dummy entry

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print result.val,
  result = result.next
# 7 0 8