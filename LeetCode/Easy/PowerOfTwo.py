import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # if n <= 0:
        #     return False
        # return math.log2(n).is_integer()
        
        # alternate way
        
        if n < 1:
            return False

        while n % 2 == 0:
            n = n // 2

        return n == 1

'''

O/P:
1  -> true
16 -> true
3  -> false

'''
