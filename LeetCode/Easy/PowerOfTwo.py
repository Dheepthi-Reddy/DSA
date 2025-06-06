import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return math.log2(n).is_integer()

'''

O/P:
1  -> true
16 -> true
3  -> false

'''
