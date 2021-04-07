## Dictionaries

- Dictionaries are used to store data values as key:value pairs where the key is always **unique**, but the key can be any value.
- They're declared using curly braces, each key:value pair is pairs with a colon, and each pair is separated with a comma (much like objects or json in javascript).
- If a duplicate key-name is used when declaring or updating a dictionary, it will replace the existing key:value pair, so that only the most recently declared key:value of that key-name will exist.
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
