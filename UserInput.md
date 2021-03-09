# User Input

The `input()` function can be used to access and assign values from the terminal:

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
