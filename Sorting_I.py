'''
Selection sort:
Selecting the minimum element and swapping with them in ascending order.

Bubble Sort:
Push the minimum element to the last by adjacent swapping.

Insertion Sort:
Takes an element and places it in correct order.

'''

class Solution_SelectionSort:
  def selectionSort(self, arr, n):
    for i in range(n-1):
      mini = i
      for j in range(i+1, n):
        if arr[j] < arr[mini]:
          mini = j
      arr[mini], arr[i] = arr[i], arr[mini]
    print("Selection Sort: ",arr)

sol = Solution_SelectionSort()
arr = [13, 46, 24, 52, 20, 9]
n = len(arr)
sol.selectionSort(arr, n)

class Solution_BubbleSort:
  def bubbleSort(self, arr, n):
    for i in range(n-1, -1, -1):
        didSwap = 0
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didSwap = 1
        # if the array is already sorted and no swapping happened then break
        if didSwap == 0:
            break 
    print("Bubble Sort: ",arr)
    
sol = Solution_BubbleSort()
arr = [13, 46, 24, 52, 20, 9]
n = len(arr)
sol.bubbleSort(arr, n)

class Solution_InsertionSort:

  def insertionSort(self, arr, n):
    for i in range(n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    print("Insertion Sort: ",arr)
    
sol = Solution_InsertionSort()
arr = [13, 46, 24, 52, 20, 9]
n = len(arr)
sol.insertionSort(arr, n)

'''
O/P:

Selection Sort:  [9, 13, 20, 24, 46, 52]
Bubble Sort:  [9, 13, 20, 24, 46, 52]
Insertion Sort:  [9, 13, 20, 24, 46, 52]

'''
