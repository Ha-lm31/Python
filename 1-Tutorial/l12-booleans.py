# 27-01-2026

## Booleans represent one of two values: True or False.
print(10 > 9)
print(10 == 9)
print(10 < 9)
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
'''
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
'''
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
'''
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "",
 the number 0, and the value None. And of course the value False evaluates to False.
'''
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))
def myFunction() :
  return True
print(myFunction())
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
## Check if an object is an integer or not
x = 200
print(isinstance(x, int))
