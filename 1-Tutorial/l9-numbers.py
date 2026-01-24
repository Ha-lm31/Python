# 24-01-2026

x = 1 #int \ integer
y = 2.8 #float \ floating point number
z = 1j #complex
print(type(x))
print(type(y))
print(type(z))
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
## Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
## Complex numbers are written with a "j" as the imaginary part
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))
## convert from int to float:
x = float(1)
#convert from float to int:
y = int(2.8)
## convert from int to complex:
z = complex(1)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
## Note: You cannot convert complex numbers into another number type.
import random
print(random.randrange(1, 10))
