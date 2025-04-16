'''
RECURSION:

When a function calls itself
Until a specified condition is met


"To repeat a task without Loops"

Infinite Recursion - without a condition the function keeps running 

Stack Overflow - Inside the stack functions wait for next function to complete the execution, 
when numerous calls wait in the stack segmentation happens which is called as Stack Overflow.

In order to prevent from segmentation we need to set a Base condition, so that the infinite rcursion stops at a point.

Problems on recursion:
1. 

'''

# 1.

class Solution:    
    #Complete this function
    def printNos(self,n):
        #Your code here
        if n == 0:
            return
        print(n, end=' ')
        self.printNos(n-1)
        

sol = Solution()
sol.printNos(10)

'''
O/P:

10 9 8 7 6 5 4 3 2 1 

'''

# 2.

class Solution:    
    #Complete this function
    def printNos(self,n):
        #Your code here
        if n == 0:
            return
        self.printNos(n-1) # Recursion, we are going deep into recursion tree before printing
        print(n, end=' ')  # Backtracking, to print from 1-10 instead of 10-1

sol = Solution()
sol.printNos(10)

'''
O/P:

1 2 3 4 5 6 7 8 9 10 

'''

# 3. Printing a name n-times

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

'''
