'''

Digits are extracted in reverse order of the number

'''

# 1. Extracting Digits
def extractedNumber(x):
    exNum = 0
    while x > 0:
        lastDigit =  x % 10
        exNum = (exNum * 10) + lastDigit
        x = x // 10
    print(exNum)

extractedNumber(3654)

'''
O/P:

4563

'''

# 2. Count of Digits
def counter(x):
    count = 0
    while x > 0:
        lastDigit =  x % 10
        count += 1
        x = x // 10
    print(count)

counter(8712345)

'''
O/P:

7

'''

# 3. Prime Number

import math

class Solution:
    def isPrime(self, n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1): # to reduce the time complexit we are running the loop till sqrt(n)
            if n % i == 0:
                return False
        return True

# Example usage:
sol = Solution()
print(sol.isPrime(31))  # True
print(sol.isPrime(1))   # False
print(sol.isPrime(37)) # False

'''

O/P:

True
False
True

'''

# 4. GCD/HCF

def findHCF(n1, n2):
    for i in range(1, min(n1+1, n2+1)):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    print(gcd)

findHCF(20, 40)

'''

O/P:

20

'''
