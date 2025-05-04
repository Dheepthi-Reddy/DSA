'''
Straght forward way to find the divisors and count of divisors.
But here the time complexity is, O(n).

'''

def allDivisors(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            print(i, end=" ")
        count += 1
    print()
    print(count)
    
allDivisors(36)

'''

O/P:

1 2 3 4 6 9 12 18 36 
36

'''

'''
To reduce the time complexity to O(sqrt(n)), we take the loop to run till sqrt of that number and store other factors.
'''

import math

def allDivisors(n):
    count = 0
    divisors = []
    for i in range(1,int(math.sqrt(n)+1)):
        if n % i == 0:
            divisors.append(i)
            if n/i != i:
                divisors.append(int(n/i))
                count += 1
        count += 1
    divisors.sort()
    print(divisors)
    print(count)
    
allDivisors(36)

'''
O/P:

[1, 2, 3, 4, 9, 12, 18, 36]
9

'''
