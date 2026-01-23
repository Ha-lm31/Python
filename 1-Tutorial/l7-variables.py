# 23-01-2026

# Variables
'''
A variable is created the moment you first assign a value to it.
'''
x = 5
y = "John"
print(x)
print(y)
'''
Variables do not need to be declared with any particular type, and can even change type after they have been set.
'''
x = 4
x = "Sally"
print(x)
## Casting
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
x = 5
y = "John"
print(type(x))
print(type(y))
x = "John"
print(x)
## double quotes are the same as single quotes:
x = 'John'
print(x)
## Variable names are case-sensitive.
a = 4
A = "Sally"
print(a)
print(A)

# Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
'''
2myvar = "John"
my-var = "John"
my var = "John"
#This example will produce an error in the result
'''
## Camel Case
myVariableName = "John"
## Pascal Case
MyVariableName = "John"
## Snake Case
my_variable_name = "John"

# Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
## Note: Make sure the number of variables matches the number of values, or else you will get an error.
x = y = z = "Orange"
print(x)
print(y)
print(z)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variable
x = "Python is awesome"
print(x)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
## Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
x = 5
y = 10
print(x + y)
'''
x = 5
y = "John"
print(x + y)
'''
x = 5
y = "John"
print(x, y)

# Global Variables
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
x = "awesome" ## local
def myfunc():
  x = "fantastic" ## global
  print("Python is " + x)
myfunc()
print("Python is " + x)
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

# Variables Excercises