class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 3 == 0:
            n = n // 3

        return n == 1

'''
O/P:

27 -> true
0  -> false
-1 -> false

'''
