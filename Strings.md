# Strings

## Strings at a glance
- The `str` class contains many handy features for dealing with strings.
- Single and double quotes can both be used. Singles are more common. A backslash escapes special characters as with Javascript (eg `\n`, `\"` and `\'`)
- Double quotes can contain single quotes and vice versa without any issues.
- Strings can span multiple lines so long as the new line is escaped by placing a backslash at the end of each breaking line.

## Immutabiity
Python strings are immutable (unlike Javascript!), so they cannot be changed once created. So - as you work with strings in Python - you create new strings every time you manipulate the value of an existing string.

For example, `'hello' + ' ' + 'world'` creates a new string `'hello world'`. After the code is evaluated there will then be four strings, the three added together and the fourth that represents the combination. None of the original strings will have changed in value.

## Accessing values in a strings
Square brackets give access to any character within a string. So where `s = 'hello'`, `s[1]` will be `'e'`.

If the index passed into the square brackets falls out of the bounds of the string python will raise an error. In this way, the Python style is to halt if it doesn't know what to do, rather than make up a default value.

The `slice` method is also handy for extracting substrings (see below).

The `len('...')` method will tell you the length of a string. eg `len('hello')` will return `5`.

Bracket notation and the `len()` method both also work on any sequence data types in python (strings, lists etc...).

Unlike other languages such as Javascript, the `+` operator does not convert numbers (or other types) into a string (type coercion).

The `print()` operator prints out one or more Python items followed by a newline. A trailing comma will omit the newline.

A "raw" string literal is prefixed with an `r`, and passes all characters through without any formatting or special treatment. For example `r'x\nx'` evaluates to the length-4 string `'x\nx'` with no newline character between x and y.

```pyhton
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
