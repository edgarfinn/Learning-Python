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

If the index passed into the square brackets falls out of the bounds of the string python will raise an error. In this respect, the Python style is to halt if it doesn't know what to do, rather than just make up a default value. 
