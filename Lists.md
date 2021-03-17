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
- `len()` can be used to return the length of a list.

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
allBools.remove(allBools[-1])
print(allBools) # [True, True]
```

## Tuples
- Tuples are very similar to lists, with the key difference that they are immutable (cannot be changed).
- Tuples are their own data type.
- Tuples are defined using parentheses.
- Values within a tuple can be referenced just the same as a list, using square bracket notation and zero- or negative-indexing.

```python
myTuple = ('one', 'two', 'three')
print(type(myTuple)) # <class 'tuple'>
print(myTuple[1]) # two
myTuple[-1] = 'last'

# Traceback (most recent call last):
#   File "myCode.py", line 4, in <module>
#     myTuple[-1] = 'last'
# TypeError: 'tuple' object does not support item assignment
```

## Sets
- Sets are used to store multiple **unique** items in a single variable. They cannot contain duplicates of any value.
- Sets are mutable; values can be added and removed.
- Sets are declared using curly braces.
- Sets can also be created by passing a list into the `set()` function.
  - Doing so will remove any duplicate values from the list.
- Sets are collections which are both `unordered` and `unindexed`; you cant reference them using an index, and you cannot expect any consistent ordering.
- The `.add()` method can be used to add values to a set.
- The `.remove()` method can be used to remove values from a set, but expects the argument to exist within the set, and will error if it doesn't.
- The `.discard()` method can also be used to remove items from a set, but does not care if tge argument exists. It will only remove it if it finds a match, and will run without problems if it doesnt find a match.

```python
mySet = {'One', 'Three', 'Two'}
mySet.add('Seven')
print(mySet) # {'Two', 'Seven', 'Three', 'One'}
mySet.remove('Three')
print(mySet) # {'Two', 'Seven', 'One'}
mySet.remove('Three')
# Traceback (most recent call last):
#   File "divisionTest.py", line 44, in <module>
#     mySet.remove('Three')
# KeyError: 'Three'
```

```python
myList = ['Nine', 'Nine', 2, 'Five']
mySet = set(myList)
print(mySet) # {'Five', 'Nine', 2}
mySet.discard('Jolene')
# note the last line does not error.
```
