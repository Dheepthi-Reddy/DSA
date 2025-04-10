'''
PalindromeNumber:

If a number is same as the initial number when arranged in reverse manner then its called a Palindrome number.

example:

343, 98789

'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        revNum = 0
        actualNum = x # storing the initial number to compare
        while x > 0:
            lastDigit =  x % 10
            revNum = (revNum * 10) + lastDigit # calculating revrse of the number
            x = x // 10 
        return actualNum == revNum

'''
O/P:

121 - true
-121 - false
10 - false

'''
