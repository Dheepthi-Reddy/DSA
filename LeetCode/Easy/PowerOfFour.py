class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 4 == 0:
            n = n // 4
        return n == 1

'''

O/P:

16 -> true
5  -> false
1  -> true

'''
