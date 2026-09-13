print("1---Python Booleans")
print("Booleans represent one of two values: True or False.")
print("1.Boolean Values")
print("10 > 9: ",10 > 9)
print("10 == 9: ",10 == 9)
print("10 < 9: ",10 < 9)
a = 200
b = 33
print(f"a: {a}, b: {b}")
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
print("2.Evaluate Values and Variables")
print('bool("Hello") :',bool("Hello"))
print("bool(15): ",bool(15))
x = "Hello"
y = 15
print(f"x : {x}, y : {y}")
print("bool(x): ",bool(x))
print("bool(y): ",bool(y))
print("3.Most Values are True & 4.Some Values are False")
print('bool("abc"): ',bool("abc"))
print("bool(123): ",bool(123))
print('bool(["apple", "cherry", "banana"]): ',bool(["apple", "cherry", "banana"]))
print("bool(False): ",bool(False))
print("bool(None): ",bool(None))
print("bool(0): ",bool(0))
print('bool(""): ',bool(""))
print("bool(()): ",bool(()))
print("bool([]): ",bool([]))
print("bool({}): ",bool({}))
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print("bool(myobj): ",bool(myobj))
print("5.Functions can Return a Boolean")
def myFunction() :
  return True
print(myFunction())
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
x = 200
print("x: ",x)
print("isinstance(x, int): ",isinstance(x, int))

print("\n2---Python Booleans Code Challenge")
