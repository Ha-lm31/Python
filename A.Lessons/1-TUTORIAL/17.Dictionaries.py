print("1---Python Dictionaries")
thisdict = {  "brand": "Ford",  "model": "Mustang",  "year": 1964}
print("Dictionaries are used to store data values in key:value pairs.")
print("A dictionary is a collection which is ordered*, changeable and do not allow duplicates.")
print(thisdict)
print('\tthisdict["brand"]: ',thisdict["brand"])
thisdict = {  "brand": "Ford",  "model": "Mustang",  "year": 1964,  "year": 2020}
print('thisdict = {  "brand": "Ford",  "model": "Mustang",  "year": 1964,  "year": 2020}: \n\t',thisdict)
print("1.Dictionary Length")
thisdict = {  "brand": "Ford",  "model": "Mustang",  "year": 1964}
print('\tlen(thisdict): ',len(thisdict))
print("2.Dictionary Items - Data Types")
thisdict = {  "brand": "Ford",  "electric": False,  "year": 1964,  "colors": ["red", "white", "blue"]}
print(thisdict)
print('\ttype(thisdict): ',type(thisdict))
print("3.The dict() Constructor")
thisdict = dict(name = "John", age = 36, country = "Norway")
print('thisdict = dict(name = "John", age = 36, country = "Norway")')
print(thisdict) 

print("\n2---Python - Access Dictionary Items")
thisdict =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
x = thisdict["model"]
print(thisdict)
print('\tx = thisdict["model"]: ',x)
x = thisdict.get("model")
print('\tx = thisdict.get("model"): ',x)
print("1.Get Keys")
x = thisdict.keys()
print('\tx = thisdict.keys(): ',x)
car = {  "brand": "Ford",  "model": "Mustang",  "year": 1964}
print(x)
x = car.keys()
print('\tx = car.keys(): ',x)
car["color"] = "white"
print('\tcar["color"] = "white": ',x)
print("2.Get Values")
thisdict = {  "brand": "Ford",  "model": "Mustang",  "year": 1964}
x = thisdict.values()
print('\tx = thisdict.values(): ',x)
car = {  "brand": "Ford",  "model": "Mustang",  "year": 1964}
x = car.values()
print('\tx = car.values(): ',x)
car["year"] = 2020
print('\tcar["year"] = 2020: ',x)
car = {  "brand": "Ford",  "model": "Mustang",  "year": 1964}
x = car.values()
print('\tx = car.values(); ',x)
car["color"] = "red"
print('\tcar["color"] = "red": ',x)
print("3.Get Items")
thisdict = {  "brand": "Ford",  "model": "Mustang",  "year": 1964}
x = thisdict.items()
print('\tx = thisdict.items(): ',x)
car = {  "brand": "Ford",  "model": "Mustang",  "year": 1964}
x = car.items()
print('\tx = car.items(): ',x)
car["year"] = 2020
print('\tcar["year"] = 2020: ',x)
x = car.items()
print('\tx = car.items(): ',x)
car["color"] = "red"
print('\tcar["color"] = "red": ',x)
print("4.Check if Key Exists")
thisdict = {  "brand": "Ford",  "model": "Mustang",  "year": 1964}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

print("\n3---Python - Change Dictionary Items")
print("1.Change Values")
thisdict =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
print(thisdict)
thisdict["year"] = 2018
print('\tthisdict["year"] = 2018: ',thisdict)
print("2.Update Dictionary")
thisdict.update({"year": 2020})
print('\tthisdict.update({"year": 2020}) :',thisdict)

print("\n4---Python - Add Dictionary Items")
print("1.Adding Items")
thisdict =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
print(thisdict)
thisdict["color"] = "red"
print('\tthisdict["color"] = "red": ',thisdict)
print("2.Update Dictionary")
thisdict.update({"country": "USA"})
print('\tthisdict.update({"color": "red"}): ',thisdict)

print("\n5---Python - Remove Dictionary Items")
thisdict =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
thisdict.pop("model")
print('\tthisdict.pop("model"): ',thisdict)
thisdict.popitem()
print('\tthisdict.popitem(): ',thisdict)
thisdict =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
del thisdict["model"]
print('\tdel thisdict["model"]: ',thisdict)
del thisdict
print("del thisdict , print(thisdict) (error)")
thisdict =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
thisdict.clear()
print('\tthisdict.clear(): ',thisdict)

print("\n6---Python - Loop Dictionaries")
thisdict =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
print("1.Print all key names in the dictionary, one by one:")
for x in thisdict:
  print('\tx: ',x)
print("2.Print all values in the dictionary, one by one:")
for x in thisdict:
  print('\tthisdict[x]: ',thisdict[x])
print("3.Use 'for x in thisdict.values():'")
for x in thisdict.values():
  print('\tx: ',x)
print("4.Use 'for x in thisdict.keys():'")
for x in thisdict.keys():
  print(x)
print("5.Use 'for x, y in thisdict.items():'")
for x, y in thisdict.items():
  print(x,',', y)

print("\n7---Python - Copy Dictionaries")
thisdict = {  "brand": "Ford",  "model": "Mustang",  "year": 1964}
mydict = thisdict.copy()
print('\tmydict = thisdict.copy(): ',mydict)
mydict = dict(thisdict)
print('\tmydict = dict(thisdict): ',mydict)

print("\n8---Python - Nested Dictionaries")
print("1.Nested Dictionaries")
print("A dictionary can contain dictionaries, this is called nested dictionaries.")
myfamily = {
  "child1" : {    "name" : "Emil",    "year" : 2004},
  "child2" : {    "name" : "Tobias",    "year" : 2007},
  "child3" : {    "name" : "Linus",    "year" : 2011}
}
print('\tmyfamily: ',myfamily)
child1 = {  "name" : "Emil",  "year" : 2004}
child2 = {  "name" : "Tobias",  "year" : 2007}
child3 = {  "name" : "Linus",  "year" : 2011}
myfamily = {  "child1" : child1,  "child2" : child2,  "child3" : child3}
print('\tmyfamily: ',myfamily)
print("2.Access Items in Nested Dictionaries")
print('\tmyfamily["child2"]["name"]: ',myfamily["child2"]["name"])
print("3.Loop Through Nested Dictionaries")
for x, obj in myfamily.items():
    print(x)    
    for y in obj:
        print(y + ':', obj[y])

print("\n9---Python Dictionary Methods")
print("Python has a set of built-in methods that you can use on dictionaries.")
print("11 methods")

print("\n10---Python Dictionary Exercises")
print("\n11---Python Dictionaries Code Challenge")