class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # if length array is smaller than k value, 
        # ex: to rotate a "single element array"(n = 1) for "2"(k = 2) times 
        k = k % n 

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)

'''
O/P:

nums = [1,2,3,4,5,6,7]
k = 3
Output: [5,6,7,1,2,3,4]

nums = [-1,-100,3,99]
k = 2
Output: [3,99,-1,-100]
'''
