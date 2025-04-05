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

