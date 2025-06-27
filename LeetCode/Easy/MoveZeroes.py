class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = -1
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                j = i
                break
        
        # when there are no zeros in the array, we exit from the function
        if j == -1:     
                return
        
        for i in range(j+1, n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

'''

(1)
Input: 
nums = [0,1,0,3,12]

Output:
[1,3,12,0,0]

(2)
Input: 
nums = [0]

Output:
[0]

(3)
Input: 
nums = [1,2,3,1]

Output:
[1,2,3,1]

'''
