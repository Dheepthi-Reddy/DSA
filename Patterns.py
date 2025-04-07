'''
Patterns:

Patterns will help in unerstanding loops better.

Outer loops -> Rows
Inner loops -> Columns

Rules to solve patterns:-
1. For outer loops, count the no.of rows
2. For inner loops, focus on the columns and connect them to rows
3. Print the desired value in the patterns
4. Observe symmetry [Optional - depending on the problem to solve]

'''

# 1.

def firstPattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end = " ")
        print()

firstPattern(4)

'''
O/P:

* * * * 

* * * * 

* * * * 

* * * * 

'''

# 2.

def secondPatern(n):
    for i in range(n):
        for j in range(i+1): 
            # if not i+1 this won't execute for n = 1
            print("*", end = " ")
        print()

secondPatern(6)

'''
O/P:

* 

* * 

* * * 

* * * * 

* * * * * 

'''

# 3.

def thirdPatern(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end = " ")
        print()

thirdPatern(6)

'''
O/P:

1 

1 2 

1 2 3 

1 2 3 4 

1 2 3 4 5 

'''

# 4.

def fourthPatern(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1, end = " ")
        print()

fourthPatern(6)

'''
O/P:

1 

2 2 

3 3 3 

4 4 4 4 

5 5 5 5 5 

'''

# 5.
def fifthPatern(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end = " ")
        print()

fifthPatern(6)

'''
O/P:

* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

'''

# 6.
def sixthPatern(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end = " ")
        print()

sixthPatern(6)

'''
O/P:

1 2 3 4 5 6 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

'''

# 7. 
def seventhPattern(n):
    for i in range(n):
        # space
        for j in range(n-i-1):
            print(" ", end = "")
        # star
        for j in range(2*i+1):
            print("*", end = "")
        print()
        
seventhPattern(6)

'''
O/P:

     *
    ***
   *****
  *******
 *********
***********

'''

# 8.
def eigthPattern(n):
    for i in range(n):
        # space
        for j in range(i):
            print(" ", end = "")
        # star
        for j in range(2*n-(2*i+1)):
            print("*", end = "")
        print()
        
eigthPattern(6)


'''
O/P:

***********
 *********
  *******
   *****
    ***
     *

'''

# 9. combination of 7th and 8th patterns
def seventhPattern(n):
    for i in range(n):
        # space
        for j in range(n-i-1):
            print(" ", end = "")
        # star
        for j in range(2*i+1):
            print("*", end = "")
        print()
        
seventhPattern(6)

def eigthPattern(n):
    for i in range(n):
        # space
        for j in range(i):
            print(" ", end = "")
        # star
        for j in range(2*n-(2*i+1)):
            print("*", end = "")
        print()
        
eigthPattern(6)

'''
O/P:

     *
    ***
   *****
  *******
 *********
***********
***********
 *********
  *******
   *****
    ***
     *

'''

# 10.

def tenthPattern(n):
    for i in range(1, 2*n):
        if(i <= n):
            stars = i
        else:
            stars = 2*n - i
        print("*" * stars)

tenthPattern(5)

'''
O/P:

*
**
***
****
*****
****
***
**
*

'''

# 11.
def eleventhPattern(n):
    for i in range(n):
        if(i%2 == 0):
            start = 1
        else:
            start = 0
        for j in range(i+1):
            print(start, end=" ")
            start = 1 - start
        print()

eleventhPattern(5)

'''
O/P:

1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 

'''
# 12.
def twelfthPattern(n):
    spaces = 2*(n-1)
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end = "")
        print(" " * spaces, end = " ")
        for j in range(i, 0, -1):
            print(j, end = "")
        print()
        spaces -= 2

twelfthPattern(5)

'''
O/P:

1         1
12       21
123     321
1234   4321
12345 54321

'''

# 13.
def thirteenthPattern(n):
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num, end = " ")
            num = num + 1
        print()

thirteenthPattern(5)

'''
O/P:

1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 

'''

# 14.

def fourteenthPattern(n):
    for i in range(n):
        for ch in range(ord('A'), ord('A')+i+1):
            print(chr(ch), end = " ")
        print()

fourteenthPattern(5)

'''
O/P:

A 
A B 
A B C 
A B C D 
A B C D E

'''


# 15.

def fifteenthPattern(n):
    for i in range(n):
        for ch in range(ord('A'), ord('A')+(n-i)):
            print(chr(ch), end = " ")
        print()

fifteenthPattern(5)


'''
O/P:

A B C D E 
A B C D 
A B C 
A B 
A 

'''

# 17.
def seventeenthPattern(n):
    for i in range(n):
         # space
        for j in range(n-i-1):
            print(" ", end = "")
        # letters
        ch = ord('A')
        breakpoint = (2*i+1)//2
        for j in range(2*i+1):
            print(chr(ch), end = " ")
            if(j < breakpoint):
                ch += 1
            else:
                ch -= 1
        print()

seventeenthPattern(5)

'''
O/P:

    A 
   A B A 
  A B C B A 
 A B C D C B A 
A B C D E D C B A 

'''

# 18.
def eigthteenthPattern(n):
    for i in range(n):
        start = ord('A')+ n -1 - i
        end = ord('A')+ n -1
        for ch in range(start, end+1):
            print(chr(ch), end = " ")
        print()

eigthteenthPattern(5)

'''
O/P:

E 
D E 
C D E 
B C D E 
A B C D E 

'''

# 19.

def nineteenthPattern(n):
    # upper half
    initialSpace = 0
    for i in range(n):
        
        # left stars
        print("*" * (n-i), end = "")
        
        # spaces
        print(" " * initialSpace, end = "")
        
        # right stars
        print("*" * (n-i))
        
        initialSpace += 2
        
    # lower half
    initialSpace = 2 * n - 2
    for i in range(1, n + 1):
        
        # left stars
        print("*" * i, end = "")
        
        # spaces
        print(" " * initialSpace, end = "")
        
        # right stars
        print("*" * i)
        
        initialSpace -= 2

nineteenthPattern(5)

'''
O/P:

**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

'''

# 20.

def twentiethPattern(n):
    
    spaces = 2 * n - 2
    
    for i in range(1, 2 * n):
        # no of stars
        if i <= n:
            stars = i
        else:
            stars = 2 * n - i
        
        # left stars
        print("*" * stars, end = "")
        # spaces
        print(" " * spaces, end = "")
        # right stars
        print("*" * stars)
        
        # updating spaces
        if i < n:
            spaces -= 2
        else:
            spaces += 2

twentiethPattern(5)

'''
O/P:

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

'''

# 21.

def twentyFirstPattern(n):
    
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n-1 or j == n-1:
                print("*", end="")
            else:
                print(" ", end = "")
        print()

twentyFirstPattern(5)

'''
O/P:

*****
*   *
*   *
*   *
*****

'''

# 22.

def twentySecondPattern(n):
    size = 2 * n - 1
    for i in range(size):
        for j in range(size):
            top = i
            left = j 
            right = (size - 1) - j
            bottom = (size - 1) - i
            
            val = n - min(top, left, right, bottom)
            print(val, end = " ")
        print()

twentySecondPattern(5)

'''
O/P:

5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5 

'''

