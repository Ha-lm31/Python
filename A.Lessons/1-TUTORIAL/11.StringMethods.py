# d-1 : 08-09-2026
print("1.capitalize() : Converts the first character to upper case")
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
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print('''txt = "Hello, And Welcome To My World!"
x = txt.casefold(): ''',x)

print("\n3.center() : Returns a centered string")
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
print("\n4.count() : Returns the number of times a specified value occurs in a string")
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print('''txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple"): ''',x)
print("Syntax : string.count(value, start, end)")
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print('''txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24): ''',x)

print("\n5.encode() : Returns an encoded version of the string")
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

print("\n6.endswith() : Returns true if the string ends with the specified value")
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

print("\n7.expandtabs() : Sets the tab size of the string")
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

print("\n8.find() : Searches the string for a specified value and returns the position of where it was found")
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

print("\n9.format() : Formats specified values in a string")
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
print("\n10.format_map() : ")
print("\n11.index() : ")
print("\n12.isalnum() : ")


'''
print('''''',x)


print("\n13.")
print("\n14.")
print("\n15.")

print("\n16.")
print("\n17.")
print("\n18.")

print("\n19.")
print("\n20.")
print("\n21.")

print("\n22.")
print("\n23.")
print("\n24.")

print("\n25.")
print("\n26.")
print("\n27.")

print("\n28.")
print("\n29.")
print("\n30.")

print("\n31.")
print("\n32.")
print("\n33.")

print("\n34.")
print("\n35.")
print("\n36.")

print("\n37.")
print("\n38.")
print("\n39.")

print("\n40.")
print("\n41.")
print("\n42.")

print("\n43.")
print("\n44.")
print("\n45.")
'''