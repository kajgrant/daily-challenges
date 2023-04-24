class Solution():
  def fibonacci(self, n):
    
    if n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    return Solution().fibonacci(n-1) + Solution().fibonacci(n-2)

n = 9
print(Solution().fibonacci(n))
# 34