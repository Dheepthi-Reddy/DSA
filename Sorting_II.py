'''
Merge Sort:

Divide and Merge.

Merge sort is the best optimized sorting algorithm.

'''

class Solution_MergeSort:
  def merge(self, arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    # Storing the elemnts in a temp array
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    # if there are elements still remaining on left side
    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    # if there are elements still remaining on right side
    while right <= high:
        temp.append(arr[right])
        right += 1

    # moving elements from temp to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]
    
  def mergeSort(self, arr, low, high):
    if low >= high:
        return
    
    mid = (low + high) // 2
    self.mergeSort(arr, low, mid)        # left half
    self.mergeSort(arr, mid + 1, high)   # right half
    self.merge(arr, low, mid, high)      # merging both halves
    

sol = Solution_MergeSort()
arr = [13, 46, 24, 52, 20, 9]
n = len(arr)
sol.mergeSort(arr, 0, n-1)
print("Merge sort:", arr)

'''
O/P:

Merge sort: [9, 13, 20, 24, 46, 52]

'''
