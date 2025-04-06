# *User Input and Output*
# 1.
print("Hello World")

'''
O/P:
Hello World
'''

# 2.
print("Type something")
x = input()
print("you typed ", x)

'''
O/P:
Type something
5
you typed  5
'''

# 3.
print("Type something")
x = input()
y = input()

print("you typed x:", x, "and y:", y )

'''
O/P:
Type something
7
8
you typed x: 7 and y: 8
'''


# *Data Types*
# 4.
x = "hey"
print(type(x))

x = 3
print(type(x))

x = 3.0
print(type(x))

x = 2j
print(type(x))


x = True
print(type(x))

x = ["apple", "banana", "mango"]
print(type(x))

x = ("apple", "banana", "mango")
print(type(x))

x = {"apple", "banana", "mango"}
print(type(x))

'''
O/P:
<class 'str'>
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'bool'>
<class 'list'>
<class 'tuple'>
<class 'set'>
'''

# *If Else statements*

# 5. Takes input of the age and returns if adult or not
print("Enter age")
age = int(input())
if(age >= 18):
    print("ADULT")
else:
    print("Not an adult")

'''
O/P:
Enter age
18
ADULT
'''

# multiple conditonal statements:
# 6.
print("Enter grade")
grade = int(input())
if(grade < 25):
    print("F")
elif(grade < 44):
    print("E")
elif(grade < 49):
    print("D")
elif(grade < 59):
    print("C")
elif(grade < 79):
    print("B")
elif(grade >= 80 and grade <= 100):
    print("A")

'''
O/P:
Enter grade
73
B
'''

# *Match Statement*
# 7.
print("Enter day of the week:")
day = int(input())

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid")

'''
O/P:
Enter day of the week:
2
Tuesday
'''

# *Arrays*
# Similar data types 
# 8.
nums = ["5", "4", "2", "6", "7"]
print(nums)

'''
O/P:
['5', '4', '2', '6', '7']
'''

# *2D-Arrays*
# 9.
nums = [["5", "4", "2"], ["6", "7", "2"], ["4", "2", "6"]]
print(nums)
nums[1][2] = 9
print(nums)

'''
O/P:
[['5', '4', '2'], ['6', '7', '2'], ['4', '2', '6']]
[['5', '4', '2'], ['6', '7', 9], ['4', '2', '6']]
'''

# *Strings*
# 10.
s = "Dheepthi"
print(s[4])
print(len(s))       # size of the string
print(s[len(s)-1])  # printing last letter of the string

t = 's'
s = s+t
print(s) 

'''
O/P:
p
8
i
Dheepthis
'''

# *For Loops*
# 11.
for i in range(5):
    print(i)
print("===")    
for i in range(0,4):
    print(i)
print("===")    
for i in range(0,7,2):
    print(i)

'''
O/P:
0
1
2
3
4
===
0
1
2
3
===
0
2
4
6
'''

# for array
# 12.
print("====Looping through string====")
for i in "fruits":
    print(i)

print("====Array====")

fruits = ["apple", "banana", "cherry"]

for i in fruits:
    print(i)

print("====Array with break====")
for i in fruits:
    print(i)
    if(i == "banana"):
        break

print("====")    
for i in fruits:
    if(i == "banana"):
        break   #stops iterateing after break
    print(i)
    
print("====Array with continue====")
for i in fruits:
    print(i)
    if(i == "banana"):
        continue

print("====")    

for i in fruits:
    if(i == "banana"):
        continue #stops for current iteration and continues
    print(i)

'''
O/P:
====Looping through string====
f
r
u
i
t
s
====Array====
apple
banana
cherry
====Array with break====
apple
banana
====
apple
====Array with continue====
apple
banana
cherry
====
apple
cherry
'''

# *While Loops*
# 13.
i = 0

while(i<6):
    print(i)
    i += 1

print("===")
i = 0
while(i<6):
    i += 1
    print(i)

print("===continue")
i = 0
while(i<6):
    i += 1
    if i == 3:
        continue
    print(i)

print("===break")
i = 0
while(i<6):
    i += 1
    if i == 3:
        break
    print(i)
    
'''
O/P:
0
1
2
3
4
5
===
1
2
3
4
5
6
===continue
1
2
4
5
6
===break
1
2
'''

# *Functions*
'''
A set of code which performs something for you
Used to modularise code
Used to increase readability
Code reusability

Types:
void
return
parameterised
non parameterised
'''
# 14.
print("====Void functions====")
def myName():
    print("Dheepthi")
    
myName()

print("====Void Parameterised function====")
def myNameInput(name):
    print("Hey", name)

print("enter your name to greet...")
name = input()
myNameInput(name)

'''
O/P:
====Void functions====
Dheepthi
====Void Parameterised function====
enter your name to greet...
reddy
Hey reddy
'''





