# User Input

## `input()` and `type()` functions
- The `input()` function can be used to access and assign values from the terminal:
- And you can use the `type()` function to determine the data type of a value

```python
#DOB.py
birthYear = input("What year were you born? \n")
print("You were born in {year}".format(year = birthYear))ash
```

```bash
#terminal
$ python3 DOB.py
# What year were you born?
1986
# You were born in 1986
```

The function defaults to expecting a string typed user input, but this can be converted using any of the normal converters `int()`, `float()` etc...:

```python
DOB.py
birthYear = int(input("What year were you born? \n"))
print("birthYear is a {dataType}".format(dataType = type(birthYear)))
```

```bash
#terminal
$ python3 DOB.py
# What year were you born?
78
# birthYear is now a <class 'int'>
```

## Try / Except
Try except is similar to Javascript's `try / catch` keywords, but is set up slightly differently

```python
#age.py
try:
    age = int(input("How old are you? \n"))
    doubleAge = age * 2
    print("{} is twice your age".format(doubleAge))
except:
    print("You must enter a valid integer")
```

```bash
#terminal
$ age.py
# How old are you?
10
# 20 is twice your age

$ age.py
# How old are you?
F
# You must enter a valid integer
```

You can also catch specific exceptions, and handle multiple different error cases, including a final catch-all error case. More information on [W3schools try / except docs](https://www.w3schools.com/python/python_try_except.asp) and this [Programiz article on python's try / except](https://www.programiz.com/python-programming/exception-handling)
