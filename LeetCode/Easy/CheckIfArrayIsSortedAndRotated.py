class Solution:
    def check(self, nums) -> bool:
        n = len(nums)
        count = 0
        for i in range(1,n):
            if nums[i] < nums[i-1]:
                count += 1
        if nums[0] < nums[-1]:
            count += 1
        return count <= 1


sol = Solution()
nums = [3,4,5,1,2]
# nums = [2,1,3,4]
# nums = [1,2,3]
print(sol.check(nums))

'''
O/P:

True
# False
# True

'''
