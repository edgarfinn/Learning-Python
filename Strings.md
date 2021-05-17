# Strings

## Strings at a glance
- The `str` class contains many handy features for dealing with strings.
- Single and double quotes can both be used. Singles are more common. A backslash escapes special characters as with Javascript (eg `\n`, `\"` and `\'`)
- Double quotes can contain single quotes and vice versa without any issues.
- Strings can span multiple lines so long as the new line is escaped by placing a backslash at the end of each breaking line.
- Unicode is supported "out of the box"

## A few basics:

- `string.upper()`
- `string.lower()`
- `string.len()`
- `string.replace(oldValue, newValue, count)`
  - Count is optional, and specifies how many occurrences of the old value you want to replace. Defaults to all.
- `string.split(separator, maxSplit)`
  - Both parameters are optional.
  - By default any whitespace is a separator.
  - MaxSplit specifies how many splits to do. Default is -1 which is all occurrences.

## Immutabiity
Python strings are immutable (unlike Javascript!), so they cannot be changed once created. So - as you work with strings in Python - you create new strings every time you manipulate the value of an existing string.

For example, `'hello' + ' ' + 'world'` creates a new string `'hello world'`. After the code is evaluated there will then be four strings, the three added together and the fourth that represents the combination. None of the original strings will have changed in value.

## Accessing values in a strings
- Square brackets give access to any character within a string. So where `s = 'hello'`, `s[1]` will be `'e'`.
- Any negative value counts backwards from the end of the string.
- Square brackets can access a range of characters, denoted by two positions separated by a colon.
- If you leave either first position or last position blank, python defaults to the highest and lowest (respectively) positions.

```python
s = "Hello World"
s[-1] # 'd'
s[0:4] # 'Hell'
s[:4] # 'Hell'
s[:-4] # 'Hello W'
s[-4:] # 'orld'
s[3:-2] # 'lo Wor'
```

- If the index passed into the square brackets falls out of the bounds of the string python will raise an error. In this way, the Python style is to halt if it doesn't know what to do, rather than make up a default value.

```python
>>> s = 'hi'
>>> s[13]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

The `slice` method is also handy for extracting substrings (see below).

The `len('...')` method will tell you the length of a string. eg `len('hello')` will return `5`.

Bracket notation and the `len()` method both also work on any sequence data types in python (strings, lists etc...).

Unlike Javascript, the `+` operator does not convert numbers (or other types) into a string (type coercion).

The `print()` operator prints out one or more Python items followed by a newline. A trailing comma will omit the newline.

A "raw" string literal is prefixed with an `r`, and passes all characters through without any formatting or special treatment. For example `r'x\nx'` evaluates to the length-4 string `'x\nx'` with no newline character between x and y.

```python
>>> s = 'hi\nthere'
>>> print(s)
hi
there
>>> s = r'hi\nthere'
>>> print(s)
hi\nthere

>>> s = 'x\ny'
>>> print(s)
x
y
>>> s = r'x\ny'
>>> print(s)
x\ny
```

Similarly, a `u` prefix allows you to write a unicode string literal.

## Formatting strings
The `format()` string method can be used to apply handy formatting, and form template strings (similar to Javascript template literals). You can call it on any string as a template, and pass in variables that are then interpreted in the string template using curlies.

```python
"My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# "My name is John, I'm 36"

"My name is {0}, I'm {1}".format("John",36)
# "My name is John, I'm 36"

"My name is {1}, I'm {0}".format("John",36)
# "My name is 36, I'm John"

"{} {}!".format("Hello", "world")
# 'Hello world!'
```
