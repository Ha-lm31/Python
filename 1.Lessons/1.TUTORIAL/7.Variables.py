print("1---Python Variables")
print("1.Variables are containers for storing data values.")
x = 5
y = "John"
print(x)
print(y)
print("2.Variables do not need to be declared with any particular type, and can even change type after they have been set.")
x = 4
x = "Sally"
print(x)
print("3.If you want to specify the data type of a variable, this can be done with casting.")
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
print("4.You can get the data type of a variable with the type() function.")
x = 5
y = "John"
print(type(x))
print(type(y))
print("double quotes are the same as single quotes")
x = "John"
print(x)
x = 'John'
print(x)
print("5.Variable names are case-sensitive.")
a = 4
A = "Sally"
print(a)
print(A)
print("A will not overwrite a")

print("\n2---Variable Names")
print('''
Rules for Python variables:
\n -A variable name must start with a letter or the underscore (_) character
\n -A variable name cannot start with a number
\n -A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
\n -Variable names are case-sensitive (age, Age and AGE are three different variables)
\n -A variable name cannot be any of the Python keywords.
''')
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
print("Legal variable names : myvar, my_var, _my_var, myVar, MYVAR, myvar2.")
'''
\n2myvar = "John"
\nmy-var = "John"
\nmy var = "John"
\n#This example will produce an error in the result
'''
print("Illegal variable names : 2myvar, my-var, my var.")
print("Multi Words Variable Names")
print("1.Camel Case : Each word, except the first, starts with a capital letter.")
print("myVariableName = 'John'")
print("2.Pascal Case : Each word starts with a capital letter.")
print("MyVariableName = 'John'")
print("3.Snake Case : Each word is separated by an underscore character.")
print("my_variable_name = 'John'")

print("\n3---Assign Multiple Values")
print("1.Python allows you to assign values to multiple variables in one line.")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print("Note: Make sure the number of variables matches the number of values, or else you will get an error.")
print("2.And you can assign the same value to multiple variables in one line.")
x = y = z = "Orange"
print(x)
print(y)
print(z)
print("3.If you have a collection of values in a list, tuple etc. \nPython allows you to extract the values into variables. \nThis is called unpacking.")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print("\n4---Output Variables")
print("1.The print() function is often used to output variables.")
x = "Python is awesome"
print(x)
print("In the print() function, you output multiple variables, separated by a comma.")
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print("You can also use the + operator to output multiple variables.")
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
print('Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".')
print("For numbers, the + character works as a mathematical operator.")
x = 5
y = 10
print(x + y)
print("In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error")
'''
\nx = 5
\ny = "John"
\nprint(x + y)
'''
print("The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types")
x = 5
y = "John"
print(x, y)

print("\n5---Global Variables")
print("1.Global variables can be used by everyone, both inside of functions and outside.")
print("##Create a variable outside of a function, and use it inside the function")
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
print("##Create a variable inside a function, with the same name as the global variable")
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
print("2.To create a global variable inside a function, you can use the global keyword.")
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
print("##To change the value of a global variable inside a function, refer to the variable by using the global keyword")
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)