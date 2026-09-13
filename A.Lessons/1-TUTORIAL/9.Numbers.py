print("1---Python Numbers")
print('''There are three numeric types in Python:
\n-int
\n-float
\n-complex''')
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print("Variable : ",x,"Type : ",type(x))
print("Variable : ",y,"Type : ",type(y))
print("Variable : ",z,"Type : ",type(z))
print("1.Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.")
x = 1
y = 35656222554887711
z = -3255522
print("Variable : ",x,"Type : ",type(x))
print("Variable : ",y,"Type : ",type(y))
print("Variable : ",z,"Type : ",type(z))
print("2.Float, or 'floating point number' is a number, positive or negative, containing one or more decimals.")
x = 1.10
y = 1.0
z = -35.59
print("Variable : ",x,"Type : ",type(x))
print("Variable : ",y,"Type : ",type(y))
print("Variable : ",z,"Type : ",type(z))
print("-Float can also be scientific numbers with an "e" to indicate the power of 10.")
x = 35e3
y = 12E4
z = -87.7e100
print("Variable : ",x,"Type : ",type(x))
print("Variable : ",y,"Type : ",type(y))
print("Variable : ",z,"Type : ",type(z))
print("3.Complex numbers are written with a 'j' as the imaginary part.")
x = 3+5j
y = 5j
z = -5j
print("Variable : ",x,"Type : ",type(x))
print("Variable : ",y,"Type : ",type(y))
print("Variable : ",z,"Type : ",type(z))
print("Type Conversion")
print("You can convert from one type to another with the int(), float(), and complex() methods.")
#convert from int to float:
x = float(1)
#convert from float to int:
y = int(2.8)
#convert from int to complex:
z = complex(1)
print("Variable : ",x,"Type : ",type(x))
print("Variable : ",y,"Type : ",type(y))
print("Variable : ",z,"Type : ",type(z))
print("##Note: You cannot convert complex numbers into another number type.")
print("Random Number")
import random
print("random.randrange(1, 10) : ",random.randrange(1, 10))

print("\n2---Python Numbers Code Challenge")