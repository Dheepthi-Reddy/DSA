'''
Hashing:
It is about Pre-storing and fetching. This concept helps in finding the frequency of a value.

Numerical Hashing:

Inside int{} we can only hash till 10^5, and globally we can hash till 10^7 using arrays

'''

n = int(input("No of elements:"))
arr = list(map(int, input().split()))

hash_array = [0] * 13

print(n)
print(arr)
print("Before:",hash_array)

for num in arr:
    hash_array[num] += 1

print("After:",hash_array)

q = int(input("No of queries:"))

for _ in range(q):
    number = int(input())
    print(hash_array[number])



'''
O/P:

No of elements:4
1 2 2 3
4
[1, 2, 2, 3]
Before: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
After: [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
No of queries:3
6
0
2
2
1
1


Charecter Hashing:

If the string has only lower case: ch - 'a'
If the string has only upper case: ch - 'A'
If the string has both: 256

'''

s = input()

hash_array = [0] * 26

print(s)
print("Before:",hash_array)

for ch in s:
    hash_array[ord(ch) - ord('a')] += 1

print("After:",hash_array)

q = int(input("No of queries:"))

for _ in range(q):
    c = input()
    print(hash_array[ord(c) - ord('a')])

'''
O/P:

appagadu
appagadu
Before: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
After: [3, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
No of queries:3
a
3
p
2
g
1


Map/Dictionaries:

When using maps we have a limitation, which is, when the input array size is huge it might not be the right choice to use a hash array for storing the frequencies.
So, we use Dictionaries in Python for storing such values. 
Because it will only store the given elements but not all the integers starting from 0 to largest elemnt of that array.

'''

n = int(input("Enter the no of elements:"))
arr = list(map(int, input("Enter array elements:").split()))

freq_map = {}

for num in arr:
  if num in freq_map:
    freq_map[num] +=1
  else:
    freq_map[num] =1

q = int(input("Enter the no of queries:"))

for _ in range(q):
  number = int(input("Enter the element to check frequency:"))
  print(freq_map.get(number, 0))

'''
O/P:

Enter the no of elements:5
Enter array elements:1 2 3 2 1
Enter the no of queries:5
Enter the element to check frequency:3
1
Enter the element to check frequency:4
0
Enter the element to check frequency:1
2
Enter the element to check frequency:45
0
Enter the element to check frequency:0
0

Example:
'''

class Solution:
    def getFrequencies(self, arr, n):
        map = {}
        
        for i in range(n):
            if arr[i] in map:
                map[arr[i]] += 1
            else:
                map[arr[i]] = 1
        for q in map:
            print(q, map[q])

sol = Solution()
arr = [10, 5, 10, 15, 10, 5]
n = len(arr)
sol.getFrequencies(arr, n)

'''
O/P:

10 3
5 2
15 1

'''
