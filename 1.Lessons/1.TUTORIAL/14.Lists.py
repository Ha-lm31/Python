print("1---Python Lists")
mylist = ["apple", "banana", "cherry"]
print("Lists are used to store multiple items in a single variable.")
print("Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.")
thislist = ["apple", "banana", "cherry"]
print('thislist = ["apple", "banana", "cherry"]')
print(thislist)
print("List items are ordered, changeable, and allow duplicate values.")
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
print("\tlen(thislist): ",len(thislist))
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
list1 = ["abc", 34, True, 40, "male"]
print(list1)
mylist = ["apple", "banana", "cherry"]
print("\ttype(mylist): ",type(mylist))
print("-Using the list() constructor to make a List: # note the double round-brackets")
thislist = list(("apple", "banana", "cherry"))
print(thislist)
print('''**Python Collections (Arrays)
*There are four collection data types in the Python programming language:
-List is a collection which is ordered and changeable. Allows duplicate members.
-Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
-Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
-Dictionary is a collection which is ordered** and changeable. No duplicate members.''')

print("\n2---Python - Access List Items")
thislist = ["apple", "banana", "cherry"]
print("\tthislist[1]: ",thislist[1])
print("\tthislist[-1]: ",thislist[-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print('thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]')
print("\tthislist[2:5]: ",thislist[2:5])
print("## Note: The search will start at index 2 (included) and end at index 5 (not included).\n Remember that the first item has index 0.")
print("\tthislist[:4]: ",thislist[:4])
print("\tthislist[2:]: ",thislist[2:])
print("\tthislist[-4:-1]: ",thislist[-4:-1])
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

print("\n3---Python - Change List Items")
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print('''thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"''')
print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(''''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]''')
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print('''thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]''')
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(''''thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]''')
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print('thislist.insert(2, "watermelon"): ',thislist) 

print("\n4---Python - Add List Items")
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print('\tthislist.append("orange"): ',thislist)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print('''thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]''')
print('\tthislist.extend(tropical): ',thislist)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
print(''''thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")''')
thislist.extend(thistuple)
print("\tthislist.extend(thistuple): ",thislist) 

print("\n5---Python - Remove List Items")
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print('\tthislist.remove("banana"): ',thislist)
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print('thislist = ["apple", "banana", "cherry", "banana", "kiwi"]')
thislist.remove("banana")
print('\tthislist.remove("banana"): ',thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print('\tthislist.pop(1): ',thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print("\tthislist.pop(): ",thislist)
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print("\tdel thislist[0]: ",thislist)
thislist = ["apple", "banana", "cherry"]
del thislist
print("del thislist\nprint(thislist): error")
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print("\tthislist.clear(): ",thislist)

print("\n6---Python - Loop Lists")
print("1.Loop Through a List")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
print("2.Loop Through the Index Numbers")
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
print("3.Using a While Loop")
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
print("4.Looping Using List Comprehension")
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

print("\n7---Python - List Comprehension")
print("List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
#or
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print('newlist = [x for x in fruits if "a" in x]:')
print('\t',newlist)
print("The Syntax : newlist = [expression for item in iterable if condition == True]")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print("Condition")
newlist = [x for x in fruits if x != "apple"]
print('newlist = [x for x in fruits if x != "apple"]: ')
print('\t',newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print('newlist = [x for x in fruits]:')
print('\t',newlist)
print("Iterable")
newlist = [x for x in range(10)]
print('newlist = [x for x in range(10)]: ')
print('\t',newlist)
newlist = [x for x in range(10) if x < 5]
print('newlist = [x for x in range(10) if x < 5]: ')
print('\t',newlist)
print("Expression")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print('newlist = [x.upper() for x in fruits]: ')
print('\t',newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print('newlist = ['hello' for x in fruits]: ')
print('\t',newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print('newlist = [x if x != "banana" else "orange" for x in fruits]:')
print('\t',newlist)
print("Return the item if it is not banana, if it is banana return orange.")

print("\n8---Python - Sort Lists")
print("1.Sort List Alphanumerically")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(thislist)
thislist.sort()
print('\tthislist.sort(): ',thislist)
thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort()
print('\tthislist.sort(): ',thislist)
print("2.Sort Descending")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(thislist)
thislist.sort(reverse = True)
print('\tthislist.sort(reverse = True): ',thislist)
thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort(reverse = True)
print('\tthislist.sort(reverse = True): ',thislist)
print("3.Customize Sort Function")
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
print("4.Case Insensitive Sort (majuscule first than minuscul)")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist)
thislist.sort()
print('\tthislist.sort(): ',thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print('\tthislist.sort(key = str.lower): ',thislist)
print("5.Reverse Order")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist)
thislist.reverse()
print('\tthislist.reverse(): ',thislist)

print("\n9---Python - Copy Lists")
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print('\tmylist = thislist.copy(): ',mylist)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print('\tmylist = list(thislist): ',mylist)
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print('\tmylist = thislist[:]: ',mylist)

print("\n10---Python - Join Lists")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
print('list1: ',list1)
print('list2: ',list2)
list3 = list1 + list2
print('\tlist3 = list1 + list2: ',list3)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print('\tlist1.extend(list2): ',list1)

print("\n11---Python - List Methods")
print("Python has a set of built-in methods that you can use on lists.")
print("11 methods")

print("\n12---Python List Exercises")
print("\n13---Python Lists Code Challenge")