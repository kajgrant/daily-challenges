def staircase(n):
    return fib(n+1)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
  
print staircase(4)
# 5
print staircase(5)
# 8