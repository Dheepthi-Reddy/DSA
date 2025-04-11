'''
If an integer has exactly three positive divisors, return True if not False.

'''

class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1
        return count == 3
        
sol = Solution()
print(sol.isThree(4))
print(sol.isThree(2))

'''

O/P:
True
False

'''
