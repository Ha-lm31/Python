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
