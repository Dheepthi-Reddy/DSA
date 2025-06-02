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

Quick Sort:

1. Pick a pivot element from the array and place it in its sorted place of the array
2. Add remaining smaller elements to the left of pivot element and larger ones on the right.
3. Repeat the steps on the left and right side for the sub arrays to the pivot element.


'''

class Solution_QuickSort:
  def partition(self, arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    
    while i < j:
        while i <= high - 1 and arr[i] <= pivot:
            i += 1
        while j >= low + 1 and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
  def quickSort(self, arr, low, high):
    if low < high:
        partition_index = self.partition(arr, low, high)
        self.quickSort(arr, low, partition_index - 1)
        self.quickSort(arr, partition_index + 1, high)

sol = Solution_QuickSort()
arr = [13, 46, 24, 9, 52, 20, 9]
n = len(arr)
sol.quickSort(arr, 0, n-1)
print("Quick Sort:", arr)

'''
O/P:

Quick Sort: [9, 9, 13, 20, 24, 46, 52]

'''
