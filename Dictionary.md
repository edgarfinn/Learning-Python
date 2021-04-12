## Dictionaries

- Dictionaries are used to store data values as `key:value` pairs where the key is always **unique**, but the value can be anything.
- They're declared using curly braces, each `key:value` pair is paired with a colon, and each pair is separated with a comma (much like objects or json in javascript).
- If a duplicate key-name is used when declaring or updating a dictionary, it will replace the existing `key:value` pair, so that only the most recently declared `key:value` of that key-name will exist.
- As of python 3.7 dictionaries are ordered, meaning they have a defined order that will not change. Prior to 3.7 dictionaries were unordered.
- Key:value pairs are changeable, so a value can be changed after it was already declared.
- Values are accessed using bracket notation.
- The `len()` function can be used to determine the length of a dictionary (ie how many key:value pairs it has)

```python
myBike = {
  "make": "Specialized",
  "model": "Rockhopper",
  "year": 2000
}
print(myBike["model"]) # Rockhopper
print(len(myBike)) # 3
myBike["year"] = 2010
print(myBike) # {'make': 'Specialized', 'model': 'Rockhopper', 'year': 2010}
```

Deleting an item from a dictionary is done using the `del()` function (similarly to lists):

```python
del(myBike['year'])
print(myBike) # {'make': 'Specialized', 'model': 'Rockhopper'}
```

### Referencing keys, values and items of a dictionary

Every python dictionary has a keys(), values() and items() method on it that returns a list-like reference to the dictionary's state. As the dictionary changes and updates, any reference to this state via these methods also updates.

Keys and values returns a list of references to the keys and values of respective the dictionary.

Items returns a set of tuples, each containing the key and the value.

```python
myBike = {
  "make": "Big",
  "model": "Bike",
  "year": 2000
}
myBikeKeys = myBike.keys()
myBikeValues = myBike.values()
myBikeItems = myBike.items()

print(myBikeKeys) # dict_keys(['make', 'model', 'year'])
print(myBikeValues) # dict_values(['Big', 'Bike', 2000])
print(myBikeItems) # dict_items([('make', 'Big'), ('model', 'Bike'), ('year', 2000)])

myBike["year"] = 2010

print(myBikeItems) # dict_items([('make', 'Big'), ('model', 'Bike'), ('year', 2010)])
```

Just like lists, you can iterate through these list-like references in a for loop:

```python
for key in myBikeKeys:
    print(key)
#   make
#   model
#   year
```
