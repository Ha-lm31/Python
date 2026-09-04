print("1---Python Data Types")
print('''
Python has the following data types built-in by default, in these categories:
\n Text Type:	str
\n Numeric Types:	int, float, complex
\n Sequence Types:	list, tuple, range
\n Mapping Type:	dict
\n Set Types:	set, frozenset
\n Boolean Type:	bool
\n Binary Types:	bytes, bytearray, memoryview
\n None Type:	NoneType
''')
print("1.You can get the data type of any object by using the type() function.")
x = 5
print(type(x)) 
print("2.Setting the Data Type:")
x = "Hello World"
print("Variable : ",x,"\nYour Type : ",type(x))
x = 20
print("Variable : ",x,"\nYour Type : ",type(x))
x = 20.5
print("Variable : ",x,"\nYour Type : ",type(x))
x = 1j
print("Variable : ",x,"\nYour Type : ",type(x))
x = ["apple", "banana", "cherry"]
print("Variable : ",x,"\nYour Type : ",type(x))
x = ("apple", "banana", "cherry")
print("Variable : ",x,"\nYour Type : ",type(x))
x = range(6)
print("Variable : ",x,"\nYour Type : ",type(x))
x = {"name" : "John", "age" : 36}
print("Variable : ",x,"\nYour Type : ",type(x))
x = {"apple", "banana", "cherry"}
print("Variable : ",x,"\nYour Type : ",type(x))
x = frozenset({"apple", "banana", "cherry"})
print("Variable : ",x,"\nYour Type : ",type(x))
x = True
print("Variable : ",x,"\nYour Type : ",type(x))
x = b"Hello"
print("Variable : ",x,"\nYour Type : ",type(x))
x = bytearray(5)
print("Variable : ",x,"\nYour Type : ",type(x))
x = memoryview(bytes(5))
print("Variable : ",x,"\nYour Type : ",type(x))
x = None
print("Variable : ",x,"\nYour Type : ",type(x))
print("3.Setting the Specific Data Type:")
x = str("Hello World")
print("Variable : ",x,"\nYour Type : ",type(x))
x = int(20)
print("Variable : ",x,"\nYour Type : ",type(x))
x = float(20.5)
print("Variable : ",x,"\nYour Type : ",type(x))
x = complex(1j)
print("Variable : ",x,"\nYour Type : ",type(x))
x = list(("apple", "banana", "cherry"))
print("Variable : ",x,"\nYour Type : ",type(x))
x = tuple(("apple", "banana", "cherry"))
print("Variable : ",x,"\nYour Type : ",type(x))
x = range(6)
print("Variable : ",x,"\nYour Type : ",type(x))
x = dict(name="John", age=36)
print("Variable : ",x,"\nYour Type : ",type(x))
x = set(("apple", "banana", "cherry"))
print("Variable : ",x,"\nYour Type : ",type(x))
x = frozenset({"apple", "banana", "cherry"})
print("Variable : ",x,"\nYour Type : ",type(x))
x = bool(5)
print("Variable : ",x,"\nYour Type : ",type(x))
x = bytes(5)
print("Variable : ",x,"\nYour Type : ",type(x))
x = bytearray(5)
print("Variable : ",x,"\nYour Type : ",type(x))
x = memoryview(bytes(5))
print("Variable : ",x,"\nYour Type : ",type(x))