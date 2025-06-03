'''
Largest Element in an Array:

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

'''
