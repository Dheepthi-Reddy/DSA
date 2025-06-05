'''
Largest Element in an Array:
===========================

Brute force approach => Sort the elements in ascending order and print the last elements.
                        Time complexity: O(NlogN)
Optimized approach => Assume that the first element is the largest and traverse through all elemens, by comparing and and replaceing the largest
                      Time complexity: O(N)
'''

class Solution:
    def largestElement(self, nums):
        largest = nums[0]
        n = len(nums)
        for i in range(n):
            if nums[i] > largest:
                largest = nums[i]
        print(largest)
        
sol = Solution()
nums = [3, 3, 6, 1]
# nums = [3, 3, 0, 99, -40]

sol.largestElement(nums)

'''
O/P:

6

# 99

Second Largest Element:
======================

Brute force approach => Sort the array in ascending order and the largest element can be at (n-2), but sometimes the array elements can be repetitive.
                        So we check if it is same as largest if not we will return it.
                        Time Complexity: O(NlogN + N)

Better approach => First we find the largest element, we declare second largest as "-1" and we start finding the second largest element by comparing
                    each element and largest with second largest element.
                     Time Complexity: O(2N)
Optimal approach => We start by taking a largest element and compare with each element, if current element is largesr than the largest,
                    we update largest element with current element and second largest with largest element.
                    
'''

class Solution:
    def secondLargest(self, arr, n):
        if n < 2:
            return -1
        
        largest = float('-inf')
        second_largest = float('-inf')
        for i in range(n):
            if arr[i] > largest:
                second_largest = largest
                largest = arr[i]
            elif (arr[i] > second_largest and arr[i] != largest):
                second_largest = arr[i]
        print("Second Largest:", second_largest)
    
    def secondSmallest(self, arr, n):
        if n < 2:
            return -1
        
        smallest = float('inf')
        second_smallest = float('inf')
        for i in range(n):
            if arr[i] < smallest:
                second_smallest = smallest
                smallest = arr[i]
            elif (arr[i] < second_smallest and arr[i] != smallest):
                second_smallest = arr[i]
        print("Second Smallest", second_smallest)
        
sol = Solution()
arr = [1, 2, 4, 7, 7, 5]
n = len(arr)

sol.secondLargest(arr, n)
sol.secondSmallest(arr, n)

'''
O/P:

Second Largest: 5
Second Smallest 2

Check if the array is sorted:
============================

By checking the adjacent elements

'''

class Solution:
  def isSorted(self, nums):
    n = len(nums)
    count = 0
    for i in range(1, n):
      if nums[i] < nums[i-1]:
        return False
      return True
sol = Solution()
nums = [1, 2, 4, 7, 7, 5]
# nums = [1, 2, 3, 4, 5]

print(sol.isSorted(nums))

'''
O/P:

False
True

'''
