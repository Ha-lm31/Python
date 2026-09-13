# d-1 : 08-09-2026
print("1.capitalize() : Converts the first character to upper case")
print("Python String capitalize() Method")
txt = "hello, and welcome to my world."
x = txt.capitalize()
print('''txt = "hello, and welcome to my world."
x = txt.capitalize(): ''',x)
txt = "python is FUN!"
x = txt.capitalize()
print('''txt = "python is FUN!"
x = txt.capitalize(): ''',x)
txt = "36 is my age."
x = txt.capitalize()
print('''txt = "36 is my age."
x = txt.capitalize(): ''',x)

print("\n2.casefold() : Converts string into lower case")
print("Python String casefold() Method")
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print('''txt = "Hello, And Welcome To My World!"
x = txt.casefold(): ''',x)

print("\n3.center() : Returns a centered string")
print("Python String center() Method")
txt = "banana"
x = txt.center(20)
print('''txt = "banana"
x = txt.center(20): ''',x)
print("Syntax : 'string.center(length, character)'")
txt = "banana"
x = txt.center(20, "O")
print('''txt = "banana"
x = txt.center(20, "O"): ''',x)

# d-2 : 10-09-2026
print("4.count() : Returns the number of times a specified value occurs in a string")
print("Python String count() Method")
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print('''txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple"): ''',x)
print("Syntax : string.count(value, start, end)")
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print('''txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24): ''',x)

print("5.encode() : Returns an encoded version of the string")
print("Python String encode() Method")
txt = "My name is Ståle"
x = txt.encode()
print('''txt = "My name is Ståle"
x = txt.encode(): ''',x)
print("Syntax : string.encode(encoding=encoding, errors=errors)")
txt = "My name is Ståle"
print('\ttxt.encode(encoding="ascii",errors="backslashreplace"): ',txt.encode(encoding="ascii",errors="backslashreplace"))
print('\ttxt.encode(encoding="ascii",errors="ignore"): ',txt.encode(encoding="ascii",errors="ignore"))
print('\ttxt.encode(encoding="ascii",errors="namereplace"): ',txt.encode(encoding="ascii",errors="namereplace"))
print('\ttxt.encode(encoding="ascii",errors="replace"): ',txt.encode(encoding="ascii",errors="replace"))
print('\ttxt.encode(encoding="ascii",errors="xmlcharrefreplace"): ',txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

print("6.endswith() : Returns true if the string ends with the specified value")
print("Python String endswith() Method")
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print('''txt = "Hello, welcome to my world."
x = txt.endswith("."): ''',x)
print("Syntax : string.endswith(value, start, end)")
x = txt.endswith("my world.")
print('x = txt.endswith("my world."): ',x)
x = txt.endswith("my world.", 5, 11)
print('x = txt.endswith("my world.", 5, 11): ',x)
txt = "Hi, welcome to my castle."
x = txt.endswith(("world.", "castle."))
print('''txt = "Hi, welcome to my castle."
x = txt.endswith(("world.", "castle.")): ''',x)

print("7.expandtabs() : Sets the tab size of the string")
print("Python String expandtabs() Method")
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print('''txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2): ''',x)
print("Syntax : string.expandtabs(tabsize)")
print(txt)
print("\ttxt.expandtabs() : ",txt.expandtabs())
print("\ttxt.expandtabs(2) : ",txt.expandtabs(2))
print("\ttxt.expandtabs(4) : ",txt.expandtabs(4))
print("\ttxt.expandtabs(10) : ",txt.expandtabs(10))

print("8.find() : Searches the string for a specified value and returns the position of where it was found")
print("Python String find() Method")
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print('''txt = "Hello, welcome to my world."
x = txt.find("welcome"): ''',x)
print("Syntax : string.find(value, start, end)")
x = txt.find("e")
print('x = txt.find("e"): ',x)
x = txt.find("e", 5, 10)
print('x = txt.find("e", 5, 10): ',x)
print('txt.find("q"): ',txt.find("q"))
print('txt.index("q"): error')

print("9.format() : Formats specified values in a string")
print("Python String format() Method")
txt = "For only {price:.2f} dollars!"
print('txt = "For only {price:.2f} dollars!"')
print('txt.format(price = 49): ',txt.format(price = 49))
print("Syntax : string.format(value1, value2...)")
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)
print('''
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)''')
print(txt1)
print(txt2)
print(txt3)
print("Formatting Types....")

###########################################################################################################
print("10.format_map() : ")
print("11.index() : ")
print("12.isalnum() : ")


'''
print('''''',x)


print("13.")
print("14.")
print("15.")

print("16.")
print("17.")
print("18.")

print("19.")
print("20.")
print("21.")

print("22.")
print("23.")
print("24.")

print("25.")
print("26.")
print("27.")

print("28.")
print("29.")
print("30.")

print("31.")
print("32.")
print("33.")

print("34.")
print("35.")
print("36.")

print("37.")
print("38.")
print("39.")

print("40.")
print("41.")
print("42.")

print("43.")
print("44.")
print("45.")
'''