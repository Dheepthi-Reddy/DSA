'''
*** RECURSION: ***

When a function calls itself
Until a specified condition is met


"To repeat a task without Loops"

Infinite Recursion - without a condition the function keeps running 

Stack Overflow - Inside the stack functions wait for next function to complete the execution, 
when numerous calls wait in the stack segmentation happens which is called as Stack Overflow.

In order to prevent from segmentation we need to set a Base condition, so that the infinite rcursion stops at a point.

Problems on recursion:
1. Print a Name 5 times

'''

class Solution:
    def printGfg(self, n):
        # Code here
        if n == 0:
            return
        self.printGfg(n-1)
        print("GFG", end=" ")


sol = Solution()
sol.printGfg(5)


'''

O/P:

GFG GFG GFG GFG GFG 


2. Print linearly from 1 to N

'''
class Solution:    
    #Complete this function
    def print1toN(self, i, n):
        #Your code here
        if i > n:
            return
        print(i, end=' ')  
        self.print1toN(i+1,n) 

sol = Solution()
sol.print1toN(1, 5)

'''
O/P:

1 2 3 4 5 

3. Print linearly from 1 to N using Backtracking

f(i+1, n) -> forward recurisve function - we can not use this

f(i-1, n) -> backward recurisve function

'''

class Solution:
    def print1toN_Backtracking(self, i, n):
       if i < 1:
           return
       self.print1toN_Backtracking(i-1, n)
       print(i, end= " ")

sol = Solution()
sol.print1toN_Backtracking(5,5)

'''
O/P:

1 2 3 4 5 

4. Print from N to 1

'''

class Solution:
    def printNto1(self, i, n):
        if i < 1:
            return
        print(i, end = " ")
        self.printNto1(i-1, n)

sol = Solution()
sol.printNto1(5,5)

'''
O/P:

5 4 3 2 1 

5. Print from N to 1 with backtracking

f(i-1, n) -> forward recurisve function - we can not use this

f(i+1, n) -> backward recurisve function

'''

class Solution:
    def printNto1_Backtracking(self, i, n):
        if i > n:
            return 
        self.printNto1_Backtracking(i+1, n)
        print(i, end = " ")

sol = Solution()
sol.printNto1_Backtracking(1,5)

'''
O/P:

5 4 3 2 1 

*** Parameterized Recursion:

we changed and printed the parameter here.
'''

class Solution:
    def sumOfNnumbers(self, i, sum):
        if i < 1:
            print(sum)
            return
        self.sumOfNnumbers(i-1, sum+i)

sol = Solution()
sol.sumOfNnumbers(5,0)

'''
O/P:

15

*** Functional Recursion:

Here we don't want the parameter to do the work, we want the function to return thevalue using parameter rather than the parameter.

'''

class Solution:
    def sumOfNnumbers(self, n):
        if n == 0:
            return 0
        return n + self.sumOfNnumbers(n - 1)

sol = Solution()
print(sol.sumOfNnumbers(5))

'''
O/P:

15

Factorial of a number with Functional recursion:

In multiplication problems we have to return 1, else there is a chance of whole solution to become 0.

'''

class Solution:
    def sumOfNnumbers(self, n):
        if n == 0:
            return 1
        return n * self.sumOfNnumbers(n - 1)

sol = Solution()
print(sol.sumOfNnumbers(5))

'''
O/P:

120

Reverse of an array using Recursion:

'''

class Solution:
    def printArray(self, arr, n):
        for i in range(n):
            print(arr[i], end = " ")
    
    def reverseArray(self, arr, first, last):
        if first < last:
            arr[first], arr[last] = arr[last], arr[first]
            self.reverseArray(arr, first + 1, last - 1)

sol = Solution()
arr = [5, 4, 3, 2, 1]
n = len(arr)

sol.reverseArray(arr, 0, n-1)
sol.printArray(arr, n)

'''
1 2 3 4 5 
'''
