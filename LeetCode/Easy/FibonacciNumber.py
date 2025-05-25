class Solution:
    def fib(self, n: int) -> int:
      if n <= 1:
        return n
      last = self.fib(n-1)
      secLast = self.fib(n-2)
      return last + secLast

'''
O/P:

2 - 1
3 - 2
4 - 3

'''
