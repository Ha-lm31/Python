print("1---Python Operators")
print("Operators are used to perform operations on variables and values.")
print("10 + 5: ",10 + 5)
sum1 = 100 + 50
sum2 = sum1 + 250
sum3 = sum2 + sum2
print('''sum1 = 100 + 50
sum2 = sum1 + 250
sum3 = sum2 + sum2''')
print(sum1)
print(sum2)
print(sum3)
print('''Python divides the operators in the following groups:
1-Arithmetic operators,
2-Assignment operators,
3-Comparison operators,
4-Logical operators,
5-Identity operators,
6-Membership operators,
7-Bitwise operators.''')

print("\n2---Python Arithmetic Operators")
print("Arithmetic operators are used with numeric values to perform common mathematical operations.")
x = 15
y = 4
print('''x = 15
y = 4''')
print("Addition (+): ",x + y)
print("Subtraction (-): ",x - y)
print("Multiplication (*): ",x * y)
print("Division (/): ",x / y)
print("Modulus (%): ",x % y)
print("Exponentiation (**): ",x ** y)
print("Floor division (//): ",x // y)
print("Division in Python")
print("""/ - Division (returns a float)
// - Floor division (returns an integer)""")

print("\n3---Python Assignment Operators")
print("Assignment operators are used to assign values to variables.")
x = 5
print("x: ",x)
x = 5
x += 3
print("x += 3 => x = x + 3: ",x)
x = 5
x -= 3
print("x -= 3 => x = x - 3: ",x)
x = 5
x *= 3
print("x *= 3 => x = x * 3: ",x)
x = 5
x /= 3
print("x /= 3 => x = x / 3: ",x)
x = 5
x %= 3
print("x %= 3 => x = x % 3: ",x)
x = 5
x //= 3
print("x //= 3 => x = x // 3: ",x)
x = 5
x **= 3
print("x **= 3 => x = x ** 3: ",x)
x = 5
x &= 3
print("x &= 3 => x = x & 3: ",x)
x = 5
x |= 3
print("x |= 3 => x = x | 3: ",x)
x = 5
x ^= 3
print("x ^= 3 => x = x ^ 3: ",x)
x = 5
x >>= 3
print("x >>= 3 => x = x >> 3: ",x)
x = 5
x <<= 3
print("x <<= 3 => x = x << 3: ",x)
print(x := 3)
print("1.The Walrus Operator")
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

print("\n4---Python Ternary Operator")
print("The ternary operator allows you to assign one value if a condition is true, and another if it is false.")
num = 6
x = "WEEKEND!" if num > 5 else "Workday"
print('''num = 6
x = "WEEKEND!" if num > 5 else "Workday": ''',x)
print("## Note: The ternary operator is not an actual operator, it is a conditional expression, or a shorthand if statement.")
print("1.Instead of Elif")
num = 6
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
print('''num = 6
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday": ''',x)

print("\n5---Python Comparison Operators")
x = 5
y = 3
print('''x = 5
y = 3''')
print("Equal: ",x == y)
print("Not equal: ",x != y)
print("Greater than: ",x > y)
print("Less than: ",x < y)
print("Greater than or equal to: ",x >= y)
print("Less than or equal to: ",x <= y)
print("Chaining Comparison Operators")
x = 5
print("x = 5)
print("\t1 < x < 10: ",1 < x < 10)
print("\t1 < x and x < 10: ",1 < x and x < 10)

print("\n6---Python Logical Operators")
print("and, or, not")
x = 5
print("x = 5")
print("\tx > 0 and x < 10: ",x > 0 and x < 10)
print("\tx < 5 or x > 10: ",x < 5 or x > 10)
print("\tnot(x > 3 and x < 10): ",not(x > 3 and x < 10))

print("\n7---Python Identity Operators")
print("is, is not")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print('''x = ["apple", "banana"]
y = ["apple", "banana"]
z = x''')
print("\tx is z: ",x is z)
print("\tx is y: ",x is y)
print("\tx == y: ",x == y)
print("\tx is not y: ",x is not y)
print('''Difference Between is and == :
\tis - Checks if both variables point to the same object in memory
\t== - Checks if the values of both variables are equal''')
x = [1, 2, 3]
y = [1, 2, 3]
print('''x = [1, 2, 3]
y = [1, 2, 3]''')
print("\tx == y: ",x == y)
print("\tx is y: ",x is y)

print("\n8---Python Membership Operators")
print("in, not in")
fruits = ["apple", "banana", "cherry"]
print('fruits = ["apple", "banana", "cherry"]')
print('\t"banana" in fruits: ',"banana" in fruits)
print('\t"pineapple" not in fruits: ',"pineapple" not in fruits)
print("Membership in Strings")
text = "Hello World"
print('text = "Hello World"')
print('\t"H" in text: ',"H" in text)
print('\t"hello" in text: ',"hello" in text)
print('\t"z" not in text: ',"z" not in text)

print("\n9---Python Bitwise Operators")
print("""& (AND),
| (OR),
^ (XOR),
~ (NOT),
<< (Zero fill left shift),
>> Signed right shift""")
print("The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0.")
print("\t6 & 3: ",6 & 3)
print("The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0.")
print("\t6 | 3: ",6 | 3)
print("The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0.")
print("\t6 ^ 3: ",6 ^ 3)
print("The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).")
print("\t~3: ",~3)
print("The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off.")
print("\t3 << 2: ",3 << 2)
print("The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.")
print("\t8 >> 2: ",8 >> 2)

print("\n10---Python Operator Precedence")
print("Operator precedence describes the order in which operations are performed.")
print("""
- () : 	Parentheses,
- ** : Exponentiation,
- +x, -x, ~x : Unary plus, unary minus, and bitwise NOT,
- *, /, //, % : Multiplication, division, floor division, and modulus,
- +, - : Addition and subtraction,
- <<, >> : Bitwise left and right shifts,
- & : Bitwise AND,
- ^ : Bitwise XOR,
- | : Bitwise OR,
- ==, !=, >, >=, <, <=, is, is not, in, not in : Comparisons, identity, and membership operators,
- not : Logical NOT,
- and : AND,
- or : 	OR.
""")
print("\t(6 + 3) - (6 + 3): ",(6 + 3) - (6 + 3))
print("\t100 - 3 ** 3: ",100 - 3 ** 3)
print("\t100 + ~3: ",100 + ~3)
print("\t100 + 5 * 3: ",100 + 5 * 3)
print("\t100 - 5 * 3: ",100 - 5 * 3)
print("\t8 >> 4 - 2: ",8 >> 4 - 2)
print("\t6 & 2 + 1: ",6 & 2 + 1)
print("\t6 ^ 2 + 1: ",6 ^ 2 + 1)
print("\t6 | 2 + 1: ",6 | 2 + 1)
print("\t5 == 4 + 1: ",5 == 4 + 1)
print("\tnot 5 == 5: ",not 5 == 5)
print("\t1 or 2 and 3: ",1 or 2 and 3)
print("\t4 or 5 + 10 or 8: ",4 or 5 + 10 or 8)
print("If two operators have the same precedence, the expression is evaluated from left to right.")
print("\t5 + 4 - 7 + 3: ",5 + 4 - 7 + 3)

print("\n11---Python Operators Code Challenge")