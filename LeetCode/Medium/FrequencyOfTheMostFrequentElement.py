'''
Finding the maximum possible frequency of an element after performing at most k operations

using sliding window technique.
'''
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        l, r = 0, 0
        freq, total = 0,0

        while r < len(nums):
            total += nums[r]

            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            freq = max(freq, r - l + 1)
            r += 1
        
        return freq

'''
O/P:

nums = [1,2,4]
k = 5
o/p: 3

nums = [1,4,8,13]
k = 5
o/p: 2

nums = [3,9,6]
k = 2
o/p: 1

'''
