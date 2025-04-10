'''
Armstrong Number:

If the number is equal to its sum of k-th power of digits of a number, then its called armstrong number.

Example:

371:
3**3 + 7**3 + 1**3 = 371 

1634:
1**4 + 6**4 + 3**4 + 4**4 = 1634

2:
2**1 = 2
'''

class Solution:
    def isArmstrong(self, n: int) -> bool:
        
        temp = n # taking temporary number to find no.of digits in it
        power = 0
        while temp > 0:
            lastDigit = temp % 10
            temp = temp // 10
            power = power + 1

        sum = 0
        num = n
        while n > 0:
            lastDigit = n % 10
            sum = sum + (lastDigit**power)  # summation of all the digits with k-th power, k is the number of digits
            n = n // 10
        
        return num == sum
'''
O/P:

153 - true

123 - falase

2 - true

'''
