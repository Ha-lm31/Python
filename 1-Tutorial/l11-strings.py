# 25-01-2026

# Strings
## You can use double or single quotes:
print("Hello")
print('Hello')
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
a = "Hello"
print(a)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
## Note: in the result, the line breaks are inserted at the same position as in the code.
a = "Hello, World!"
## Get the character at position 1 (remember that the first character has the position 0)
print(a[1])
for x in "banana":
  print(x) 
a = "Hello, World!"
print(len(a))
txt = "The best things in life are free!"
print("free" in txt)
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
txt = "The best things in life are free!"
print("expensive" not in txt)
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# 26-01-2026
# Slicing Strings
## Get the characters from position 2 to position 5 (not included)
b = "Hello, World!"
print(b[2:5])
## Note: The first character has index 0.
## Get the characters from the start to position 5 (not included)
b = "Hello, World!"
print(b[:5])
## Get the characters from position 2, and all the way to the end
b = "Hello, World!"
print(b[2:])
"""Get the character
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):"""
b = "Hello, World!"
print(b[-5:-2])

# Modify Strings
## majuscule
a = "Hello, World!"
print(a.upper())
## minuscule
a = "Hello, World!"
print(a.lower())
## removes any whitespace from the beginning or the end
a = " Hello, World! "
print(a.strip())
## method replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))
## method splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
b = a.split(",")
print(b)

# Concatenate Strings
a = "Hello"
b = "World"
c = a + b
print(c)
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Format Strings
'''
age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)
'''
## But we can combine strings and numbers by using f-strings or the format() method!
"""
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as 
placeholders for variables and other operations.
"""
age = 36
txt = f"My name is John, I am {age}"
print(txt)
## A placeholder can contain variables, operations, functions, and modifiers to format the value.
price = 59
txt = f"The price is {price} dollars"
print(txt)
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
txt = f"The price is {20 * 59} dollars"
print(txt)

# Escape Characters
"""
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
"""
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
## Single Quote
txt = 'It\'s alright.'
print(txt)
## Backslash
txt = "This will insert one \\ (backslash)."
print(txt)
## New Line
txt = "Hello\nWorld!"
print(txt)
## Carriage Return
txt = "Hello\rWorld!"
print(txt)
## Tab
txt = "Hello\tWorld!"
print(txt)
## Backspace : This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)
## \f	Form Feed
## Octal value : A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)
## Hex value : A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

# Strings Methods
## Note: All string methods return new values. They do not change the original string.
"""
Method	Description

1- capitalize() : Converts the first character to upper case,
2- casefold() : Converts string into lower case,
3- center() : Returns a centered string,
4- count() : Returns the number of times a specified value occurs in a string,
5- encode() : Returns an encoded version of the string,

6- endswith() : Returns true if the string ends with the specified value,
7- expandtabs() : Sets the tab size of the string,
8- find() : Searches the string for a specified value and returns the position of where it was found,
9- format() : Formats specified values in a string,
10- format_map() : Formats specified values in a string,

index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals

isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable

isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string

lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value

rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list

rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string

swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

"""

# Strings Exercises
