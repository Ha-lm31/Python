## 26-01-2026

# 1- capitalize() : Converts the first character to upper case,
## Upper case the first letter in this sentence: 
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
txt = "python is FUN!"
x = txt.capitalize()
print (x)
txt = "36 is my age."
x = txt.capitalize()
print (x)

# 2- casefold() : Converts string into lower case,
## Make the string lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

# 3- center() : Returns a centered string,
## Print the word "banana", taking up the space of 20 characters, with "banana" in the middle
txt = "banana"
x = txt.center(20)
print(x)
## Syntax : string.center(length, character)
txt = "banana"
x = txt.center(20, "O")
print(x)

# 4- count() : Returns the number of times a specified value occurs in a string,
## Return the number of times the value "apple" appears in the string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
## Syntax : string.count(value, start, end)
## Search from position 10 to 24
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

# 5- encode() : Returns an encoded version of the string,
## UTF-8 encode the string
txt = "My name is Ståle"
x = txt.encode()
print(x)
## Syntax : string.encode(encoding=encoding, errors=errors)
## These examples uses ascii encoding, and a character that cannot be encoded, showing the result with different errors:
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

#___________________________________________________________________________________________________________________________________

# 6- endswith() : Returns true if the string ends with the specified value,
## Check if the string ends with a punctuation sign (.)
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
## Syntax : string.endswith(value, start, end)
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)
txt = "Hi, welcome to my castle."
x = txt.endswith(("world.", "castle."))
print(x)

# 7- expandtabs() : Sets the tab size of the string,
## Set the tab size to 2 whitespaces
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
## Syntax : string.expandtabs(tabsize)
txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

# 8- find() : Searches the string for a specified value and returns the position of where it was found,
## Where in the text is the word "welcome"?
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
## Syntax : string.find(value, start, end)
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)
txt = "Hello, welcome to my world."
print(txt.find("q"))
#print(txt.index("q"))

# 9- format() : Formats specified values in a string,
## Insert the price inside the placeholder, the price should be in fixed point, two-decimal format
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
## Syntax : string.format(value1, value2...)
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)
'''
:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format
'''
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "<" to left-align the value:
txt = "We have {:<8} chickens."
print(txt.format(49))

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use ">" to right-align the value:
txt = "We have {:>8} chickens."
print(txt.format(49))

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "^" to center-align the value:
txt = "We have {:^8} chickens."
print(txt.format(49))

#To demonstrate, we insert the number 8 to specify the available space for the value.
#Use "=" to place the plus/minus sign at the left most position:
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))

#Use "+" to always indicate if the number is positive or negative:
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))

#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))

#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))

#Use "," to add a comma as a thousand separator:
txt = "The universe is {:,} years old."
print(txt.format(13800000000))

#Use "_" to add a underscore character as a thousand separator:
txt = "The universe is {:_} years old."
print(txt.format(13800000000))

#Use "b" to convert the number into binary format:
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))

#Use "d" to convert a number, in this case a binary number, into decimal number format:
txt = "We have {:d} chickens."
print(txt.format(0b101))

#Use "e" to convert a number into scientific number format (with a lower-case e):
txt = "We have {:e} chickens."
print(txt.format(5))

#Use "E" to convert a number into scientific number format (with an upper-case E):
txt = "We have {:E} chickens."
print(txt.format(5))

#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:
txt = "The price is {:.2f} dollars."
print(txt.format(45))
#without the ".2" inside the placeholder, this number will be displayed like this:
txt = "The price is {:f} dollars."
print(txt.format(45))

#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))

#same example, but with a lower case f:
txt = "The price is {:f} dollars."
print(txt.format(x))

#Use "o" to convert the number into octal format:
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))

#Use "x" to convert the number into Hex format:
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))

#Use "X" to convert the number into upper-case Hex format:
txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))

#Use "%" to convert the number into a percentage format:
txt = "You scored {:%}"
print(txt.format(0.25))
#Or, without any decimals:
txt = "You scored {:.0%}"
print(txt.format(0.25))

# 10- format_map() : Formats specified values in a string,
## Insert the name and age from a dictionary into the placeholders.
myvar = {"name" : "Jane", "age" : 36}
txt = "Happy birthday {name} you are now on level {age}!"
print(txt.format_map(myvar))
## Syntax : string.format_map(dictionary)

