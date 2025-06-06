class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        for j in range(1, n):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                
        return i + 1

nums = [1, 1, 2]
sol = Solution()
new_length = sol.removeDuplicates(nums)

# to print unique elements
print(nums[:new_length])

'''
nums = [1,1,2]
Output = [1,2]

nums = [0,0,1,1,1,2,2,3,3,4]
Output = [0,1,2,3,4]
'''
