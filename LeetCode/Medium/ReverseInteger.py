'''
Calculating Revsrse of a number:

example: 

234 -> 432

5678 -> 8765

'''

class Solution:

    def reverse(self, x: int) -> int:
        revNum = 0
        negative = x < 0
        x = abs(x) # converting value to absolute integer
        while x:
            lastDigit = x % 10
            revNum = (revNum * 10) + lastDigit # finding the revrse of a number
            x = x//10
        if negative:
            revNum = -revNum # handling the absolute integer with the appropriate sign 
        
        if revNum < -2**31 or revNum > 2**31 - 1:
            return 0 # returning 0 if x crossed 32 bit integer range
        return revNum   

'''
O/P:

123 -> 321

-123 -> -321

120 -> 12
'''
