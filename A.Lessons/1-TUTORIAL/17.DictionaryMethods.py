#d-1 : 17-09-2026
print("Python Dictionary Methods")
print("1.clear() : Removes all the elements from the dictionary")
car =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
print(car)
car.clear()
print('\tcar.clear(): ',car)
print("Syntax : dictionary.clear()")

print("\n2.copy() : Returns a copy of the dictionary")
car =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
print(car)
x = car.copy()
print('\tx = car.copy(): ',x)
print("Syntax : dictionary.copy()")

print("\n3.fromkeys() : Returns a dictionary with the specified keys and value")
x = ('key1', 'key2', 'key3')
y = 0
print("""x = ('key1', 'key2', 'key3')
y = 0""")
thisdict = dict.fromkeys(x, y)
print('\tthisdict = dict.fromkeys(x, y): ',thisdict)
print("Syntax : dict.fromkeys(keys, value)")
thisdict = dict.fromkeys(x)
print('\tthisdict = dict.fromkeys(x): ',thisdict)

print("\n4.get() : Returns the value of the specified key")
car =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
x = car.get("model")
print('\tx = car.get("model"): ',x)
print("Syntax : dictionary.get(keyname, value)")
x = car.get("price", 15000)
print('\tx = car.get("price", 15000): ',x)
print('\t',car,'Not changed')

print("\n5.items() : Returns a list containing a tuple for each key value pair")
car =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
x = car.items()
print('\tx = car.items(): ',x)
print("Syntax : dictionary.items()")
car["year"] = 2018
print('car["year"] = 2018')
print('\tx = car.items(): ',x)

print("\n6.keys() : Returns a list containing the dictionary's keys")
car =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
x = car.keys()
print('\tx = car.keys(): ',x)
print("Syntax : dictionary.keys()")
car["color"] = "white"
print('car["color"] = "white"')
print('\tx = car.keys(): ',x)

print("\n7.pop() : Removes the element with the specified key")
car =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
car.pop("model")
print('\tcar.pop("model"): ',car)
print("Syntax : dictionary.pop(keyname, defaultvalue)")
car =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
x = car.pop("model")
print('\tx = car.pop("model"): ',x)

print("\n8.popitem() : Removes the last inserted key-value pair")
car =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
car.popitem()
print('\tcar.popitem(): ',car)
print("Syntax : dictionary.popitem()")
car =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
x = car.popitem()
print('\tx = car.popitem(): ',x)

print("\n9.setdefault() : Returns the value of the specified key. If the key does not exist: insert the key, with the specified value")
car =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
x = car.setdefault("model", "Bronco")
print('\tx = car.setdefault("model", "Bronco"): ',x)
print("Syntax : dictionary.setdefault(keyname, value)")
x = car.setdefault("color", "White")
print('\tx = car.setdefault("color", "White"): ',x)

print("\n10.update() : Updates the dictionary with the specified key-value pairs")
car =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
car.update({"color": "White"})
print('\tcar.update({"color": "White"}): ',car)
print("Syntax : dictionary.update(iterable)")

print("\n11.values() : Returns a list of all the values in the dictionary")
car =	{  "brand": "Ford",  "model": "Mustang",  "year": 1964}
x = car.values()
print('\tx = car.values(): ',x)
print("Syntax : dictionary.values()")
car["year"] = 2018
print('\tcar["year"] = 2018: ',x)