## Lists
Lists are commonly otherwise known as 'arrays' in many other programming languages, and behave much the same as javascript arrays.

#### At a glance:
- Lists are defined using square bracket notation
- You can place any combination of values and data types inside a list without problem
- Lists are zero-indexed
- Values within a list can be referred to using square bracket and index notation `myList[0]`
  - Negative values will refer to positions counting backwards from the end of the list.
- Lists are their own data type (unlike Javascript arrays which are generally conflated with / typed as objects)

```python
myList = [0, 'one', 2.0, True]
print(myList[0]) # 0
print(myList[1]) # one
print(myList[-1]) # True
print(type(myList)) # <class 'list'>
```
#### Methods and Functions:
- `list.append(value)` appends a value to the end of a list.
- `list.insert(index, value)` inserts a value at the given index of a list, shifting any subsequent values further up the list.
- square bracket notation can be used to set or replace the value at a given position of a list.
- The `del(listName[index])` function can be used to delete the value stored at a given index of a given list.
- `list.remove(value)` searches and removes (*only*) the first instance of a given value in a list.

```python
drinks = ['beer', 'wine', 'cocktail']
drinks.append('whiskey')
print(drinks) # ['beer', 'wine', 'cocktail', 'whiskey']

drinks.insert(1, 'crisps')
print(drinks) # ['beer', 'crisps', 'wine', 'cocktail', 'whiskey']

drinks[3] = 'crisps'
print(drinks) # ['beer', 'crisps', 'wine', 'crisps', 'whiskey']
drinks.remove('crisps')
print(drinks) # ['beer', 'white wine', 'whiskey']
```

```python
allBools = [True, False, True, False]
allBools.remove(False)
print(allBools) # [True, True, False]
```
