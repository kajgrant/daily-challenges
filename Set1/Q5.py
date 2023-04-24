class Solution: 
  def getRange(self, arr, target):
    
    first = -1
    last = -1

    for i in range(len(arr)):

        if arr[i] == target and first < 0:
            first = i
        if arr[i] == target and first > -1:
            last = i

    if first < 0 and last < 0:
        return [first]

    return [first, last]
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]