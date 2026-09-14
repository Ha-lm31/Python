print("1---Python Sets")
myset = {"apple", "banana", "cherry"}
print("Sets are used to store multiple items in a single variable.")
thisset = {"apple", "banana", "cherry"}
print(thisset)
print("## Note: the set list is unordered, meaning: the items will appear in a random order.\nRefresh this page to see the change in the result.")
print("Set items are unordered, unchangeable, and do not allow duplicate values.")
thisset = {"apple", "banana", "cherry", "apple"}
print('\tthisset = {"apple", "banana", "cherry", "apple"}: ',thisset)
thisset = {"apple", 0, "banana",False, "cherry", True, 1, 2}
print("True and 1 is considered the same value, False and 0 is considered the same value")
print('\tthisset = {"apple", 0, "banana",False, "cherry", True, 1, 2}: ',thisset)
print("1.Get the Length of a Set")
thisset = {"apple", "banana", "cherry"}
print('\tlen(thisset): ',len(thisset))
print("2.Set Items - Data Types")
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
set1 = {"abc", 34, True, 40, "male"}
print(set1)
myset = {"apple", "banana", "cherry"}
print('\ttype(myset): ',type(myset))
print("3.The set() Constructor")
thisset = set(("apple", "banana", "cherry"))
print('thisset = set(("apple", "banana", "cherry"))')
print(thisset)

print("\n2---Python - Access Set Items")
print("You cannot access items in a set by referring to an index or a key.")
thisset = {"apple", "banana", "cherry"}
print(thisset)
for x in thisset:
  print(x)
print('\t"banana" in thisset: ',"banana" in thisset)
print('\t"banana" not in thisset: ',"banana" not in thisset)

print("\n3---Python - Add Set Items")
print("1.Add Items")
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
print('\tthisset.add("orange"): ',thisset)
print("2.Add Sets")
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
print(thisset,'\n',tropical)
thisset.update(tropical)
print('\tthisset.update(tropical): ',thisset)
print("3.Add Any Iterable")
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
print(thisset,'\n',mylist)
thisset.update(mylist)
print('\tthisset.update(mylist): ',thisset)

print("\n4---Python - Remove Set Items")
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.remove("banana")
print('\tthisset.remove("banana"): ',thisset)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print('\tthisset.discard("banana"): ',thisset)
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print('\tx = thisset.pop(): ',x)
print('\tthisset: ',thisset)
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print('\tthisset.clear(): ',thisset)
thisset = {"apple", "banana", "cherry"}
del thisset
print('\tdel thisset : thisset (error)')

print("\n5---Python - Loop Sets")
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

print("\n6---Python - Join Sets")
print("1.Union")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
print(set1,'\n',set2)
set3 = set1.union(set2)
print('\tset3 = set1.union(set2): ',set3)
set3 = set1 | set2
print('\tset3 = set1 | set2: ',set3)
print("2.Join Multiple Sets")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
print(set1,'\n',set2,'\n',set3,'\n',set4)
myset = set1.union(set2, set3, set4)
print('\tmyset = set1.union(set2, set3, set4): ',myset)
myset = set1 | set2 | set3 |set4
print('\tmyset = set1 | set2 | set3 |set4: ',myset)
print("3.Join a Set and a Tuple")
x = {"a", "b", "c"}
y = (1, 2, 3)
print(x,'\n',y)
z = x.union(y)
print('\tz = x.union(y)! ',z)
print("4.Update")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
print(set1,'\n',set2)
set1.update(set2)
print('\tset1.update(set2): ',set1)
print("5.Intersection")
print("Keep ONLY the duplicates")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print(set1,'\n',set2)
set3 = set1.intersection(set2)
print('\tset3 = set1.intersection(set2): ',set3)
set3 = set1 & set2
print('\tset3 = set1 & set2: ',set3)
set1.intersection_update(set2)
print('\tset1.intersection_update(set2): ',set1)
print('The values True and 1 are considered the same value. The same goes for False and 0.')
print("6.Difference")
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print('\tset3 = set1.difference(set2): ',set3)
set3 = set1 - set2
print('\tset3 = set1 - set2: ',set3)
set1.difference_update(set2)
print('\nset1.difference_update(set2): ',set1)
print("7.Symmetric Differences")
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print('\tset3 = set1.symmetric_difference(set2): ',set3)
set3 = set1 ^ set2
print('\tset3 = set1 ^ set2: ',set3)
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print('\tset1.symmetric_difference_update(set2): ',set1)

print("\n7---Python frozenset")
print("frozenset is an immutable version of a set.")
x = frozenset({"apple", "banana", "cherry"})
print('x = frozenset({"apple", "banana", "cherry"}): ',x)
print('type(x): ',type(x)) 
print("Frozenset Methods")
print("8 methods")
#######
fs = frozenset({1, 2, 3})
cp = fs.copy()
print(fs)
print('\tcp = fs.copy(): ',cp)
a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a,'\n',b)
print('\ta.difference(b): ',a.difference(b))
print('\ta - b: ',a - b)
a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a,'\n',b)
print('\ta.intersection(b): ',a.intersection(b))
print('\ta & b: ',a & b)
a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a,'\n',b,'\n',c)
print('\ta.isdisjoint(b): ',a.isdisjoint(b))
print('\ta.isdisjoint(c): ',a.isdisjoint(c))
a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a,'\n',b)
print('\ta.issubset(b): ',a.issubset(b))
print('\ta <= b: ',a <= b)
print('\ta < b: ',a < b)
a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a,'\n',b)
print('\ta.issuperset(b): ',a.issuperset(b))
print('\ta >= b: ',a >= b)
print('\ta > b: ',a > b)
a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(a,'\n',b)
print('\ta.symmetric_difference(b): ',a.symmetric_difference(b))
print('\ta ^ b: ',a ^ b)
a = frozenset({1, 2})
b = frozenset({2, 3})
print(a,'\n',b)
print('\ta.union(b): ',a.union(b))
print('\ta | b: ',a | b)

print("\n8---Python - Set Methods")
print("Python has a set of built-in methods that you can use on sets.")
print("17 methods (all deja vu)")

print("\n9---Python - Set Exercises")
print("\n10---Python Sets Code Challenge")