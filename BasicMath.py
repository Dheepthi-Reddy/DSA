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
