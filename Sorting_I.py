'''
Selection sort:

Selecting the minimum element and swapping with them in ascending order

'''

class Solution:
  def selectionSort(self, arr, n):
    for i in range(n-1):
      mini = i
      for j in range(i+1, n):
        if arr[j] < arr[mini]:
          mini = j
      temp = arr[mini]
      arr[mini] = arr[i]
      arr[i] = temp
    print(arr) 

sol = Solution()
arr = [13, 46, 24, 52, 20, 9]
n = len(arr)
sol.selectionSort(arr, n)

'''
O/P:

[9, 13, 20, 24, 46, 52]

'''
