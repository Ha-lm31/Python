print("1---Python Strings")
print("Strings in python are surrounded by either single quotation marks, or double quotation marks.")
print("Hello")
print('Hello')
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
print("1.Assign String to a Variable")
a = "Hello"
print(a)
print("2.Multiline Strings")
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
print("## Note: in the result, the line breaks are inserted at the same position as in the code.")
print("3.Strings are Arrays (Les chaînes de caractères sont des tableaux.)")
a = "Hello, World!"
print("\ta: ",a)
print("\ta[1]: ",a[1])
print("4.Looping Through a String")
for x in "banana":
  print(x) 
print("5.String Length")
print("\tlen(a): ",len(a))
print("6.Check String")
txt = "The best things in life are free!"
print("\ttxt: ",txt)
print('\t"free" in txt: ',"free" in txt)
if "free" in txt:
  print("Yes, 'free' is present.")
print("7.Check if NOT")
print('\t"expensive" not in txt: ',"expensive" not in txt)
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

print("\n2---Python - Slicing Strings")
print("1.You can return a range of characters by using the slice syntax.")
b = "Hello, World!"
print("\tb : ",b)
print("\tb[2:5] :",b[2:5])
print("## Note: The first character has index 0.")
print("2.Slice From the Start")
print("\tb[:5] : ",b[:5])
print("3.Slice To the End")
print("\tb[2:] : ",b[2:])
print("4.Negative Indexing")
print("\tb[-5:-2] : ",b[-5:-2])

print("\n3---Python - Modify Strings")
print("Python has a set of built-in methods that you can use on strings.\n(Python possède un ensemble de méthodes intégrées que vous pouvez utiliser sur les chaînes de caractères.)")
a = "Hello, World!"
print("\na :",a)
print("1.Upper Case")
print("\ta.upper(): ",a.upper())
print("2.Lower Case")
print("\ta.lower(): ",a.lower())
print("3.Remove Whitespace")
a = " Hello, World! "
print("\ta: ",a)
print("\ta.strip()",a.strip())
print("4.Replace String")
a = "Hello, World!"
print("\na :",a)
print('\ta.replace("H", "J"):',a.replace("H", "J"))
print("5.Split String")
print('\ta.split(","): ',a.split(","))
print("6.String Methods : Learn more about String Methods with our String Methods Reference.")

print("\n4---Python - String Concatenation")
print("To concatenate, or combine, two strings you can use the + operator.")
a = "Hello"
b = "World"
c = a + b
print("\ta: ",a)
print("\tb: ",b)
print("\tc = a + b: ",c)
a = "Hello"
b = "World"
c = a + " " + b
print("\ta: ",a)
print("\tb: ",b)
print('\tc = a + " " + b: ',c)

print("\n5---Python - Format - Strings")
print("As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:")
print('''age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt) ''')
print("But we can combine strings and numbers by using f-strings or the format() method!")
print("1.F-Strings")
age = 36
txt = f"My name is John, I am {age}"
print(txt)
print("2.Placeholders and Modifiers")
price = 59
txt = f"The price is {price} dollars"
print(txt)
txt = f"The price is {price:.2f} dollars"
print(txt)
txt = f"The price is {20 * 59} dollars"
print(txt)

print("\n6---Python - Escape Characters")
print("An escape character is a backslash \ followed by the character you want to insert.")
print('''txt = "We are the so-called "Vikings" from the north."
# You will get an error if you use double quotes inside a string that are surrounded by double quotes:''')
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 
print("Escape Characters")
txt = 'It\'s alright.'
txt = "This will insert one \\ (backslash)."
txt = "Hello\nWorld!"
txt = "Hello\rWorld!"
txt = "Hello\tWorld!"
#This example erases one character (backspace):
txt = "Hello \bWorld!"
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"

print("\n7---String Methods")
print("## Note: All string methods return new values. They do not change the original string.")
print("45 methods")
print("\n8---Python - String Exercises")

print("\n9---Python Strings Code Challenge")
