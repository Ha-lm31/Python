# 08-03-2026

# Operators
print("10 + 5 = ",10 + 5)
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
print(sum1)
print(sum2)
print(sum3)
# Arithmetic Operators
x = 15
y = 4
print("x = 15\ny = 4")
print("x + y = ",x + y)
print("x - y = ",x - y)
print("x * y = ",x * y)
print("x / y = ",x / y)
print("x % y = ",x % y)
print("x ** y = ",x ** y)
print("x // y = ",x // y)
# / - Division (returns a float)
# // - Floor division (returns an integer)
x = 12
y = 5
print("x = 12\ny = 5")
print("x / y = ",x / y)
print("x // y = ",x // y)
# Assignment Operators
"""
________________________________________________
   Operator   | Example      | Same As          |
______________|______________|__________________|
   =          |  x = 3       |  x = 3           |
   +=         |  x += 3      |  x = x + 3       |
   -=         |  x -= 3      |  x = x - 3       |
   *=         |  x *= 3      |  x = x * 3       |
   /=         |  x /= 3      |  x = x / 3       |
   %=         |  x %= 3      |  x = x % 3       |
   //=        |  x //= 3     |  x = x // 3      |
   **=        |  x **= 3     |  x = x ** 3      |
   &=         |  x &= 3      |  x = x & 3       |
   |=         |  x |= 3      |  x = x | 3       |
   ^=         |  x ^= 3      |  x = x ^ 3       |
   >>=        |  x >>= 3     |  x = x >> 3      |
   <<=        |  x <<= 3     |  x = x << 3      |
   :=         |  print(x:=3) |  x = 3 print(x)  |
______________|______________|__________________|
"""
numbers = [1, 2, 3, 4, 5]
print("numbers = [1, 2, 3, 4, 5]")
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")
# Comparison Operators
"""  
___________________________________________
Operator |     Name              | Example |
_________|_______________________|_________|
 ==      | Equal                 | x == y  |
 !=      | Not equal             | x != y  |
 >       | Grater than           | x > y   |
 <       | Less than             | x < y   |
 >=      | Greater than or equal | x >= y  |
 <=      | Less than or equal    | x <= y  |
_________|_______________________|_________|
"""
x = 5
y = 3
print("x = 5\n y = 3 ")
print("x == y : ",x == y)
print("x != y : ",x != y)
print("x > y : ",x > y)
print("x < y : ",x < y)
print("x >= y : ",x >= y)
print("x <= y : ",x <= y)
x = 5
print("x = 5")
print("1 < x < 10 : ",1 < x < 10)
print("1 < x and x < 10 : ",1 < x and x < 10)
# Logical Operators
'''
and : t and t = t
or : t or - = t
not : not(t) = f
''' 
x = 5
print("x = 5")
print("x > 0 and x < 10 : ",x > 0 and x < 10)
print("x < 5 or x > 10 : ",x < 5 or x > 10)
print("not(x > 3 and x < 10) : ",not(x > 3 and x < 10))
# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print('x = ["apple", "banana"] \ny = ["apple", "banana"] \nz = x')
print("x is z : ",x is z)
print("x is y : ",x is y)
print("x == y : ",x == y)
x = ["apple", "banana"]
y = ["apple", "banana"]
print('x = ["apple", "banana"]\ny = ["apple", "banana"]')
print("x is not y : ",x is not y)
x = [1, 2, 3]
y = [1, 2, 3]
print("x = [1, 2, 3]\ny = [1, 2, 3]")
print("x == y : ",x == y)
print("x is y : ",x is y)
""""
is - Checks if both variables point to the same object in memory
== - Checks if the values of both variables are equal
"""

# Membership Operators
fruits = ["apple", "banana", "cherry"]
print('fruits = ["apple", "banana", "cherry"]')
print('"banana" in fruits : ',"banana" in fruits)
fruits = ["apple", "banana", "cherry"]
print('fruits = ["apple", "banana", "cherry"]')
print('"pineapple" not in fruits : ',"pineapple" not in fruits)
text = "Hello World"
print('text = "Hello World"')
print('"H" in text : ',"H" in text)
print('"hello" in text : ',"hello" in text)
print('"z" not in text : ',"z" not in text)

# Bitwise Operators
"""
& : ANd
| : OR
^ : XOR
~ : NOT
<< : Zero fill left shift
>> : Signed right shift
"""
# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
print("AND = & : 1&1=1 , 1&0=0&0=0")
print("6 & 3 : ",6 & 3)
# The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0
print("OR = | : 1|1=1|0=1 , 0|0=0")
print("6 | 3 : ",6 | 3)
# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0
print("XOR = ^ : 1^1=0^0=0 , 1^0=1")
print("6 ^ 3 : ",6 ^ 3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).
Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100
Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""
print("~3 : ",~3)
"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:
If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100
"""
print("3 << 2 : ",3 << 2)
"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.
If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010
"""
print("8 >> 2 : ",8 >> 2)

# Operators Presedence
"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""
print((6 + 3) - (6 + 3))
"""
Multiplication has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + 15 = 115
"""
print(100 + 5 * 3)
'''
(),
**,
+x, -x, ~x,
*, /, //, %,
+, -,
<<, >>,
&,
^,
|,
==, !=, >, >=, <, <=, is, is not, in, not in,
not,
and ,
or
'''
"""
Additions and subtractions have the same precedence, and we need to calculate from left to right.
The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
"""
print(5 + 4 - 7 + 3)