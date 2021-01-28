# If Statements, Comparisons and Boolean basics

Booleans are capitalised keywords.
```python
True
False
```

## Comparison operators

| Operator | Name  | Syntax |
| -------- | ----  | ------ |
| ==	| Equal | x == y |
| ==	| Equal |	x == y |
| !=	| Not equal	| x != y	|
| >	| Greater than	| x > y	|
| <	| Less than	 | x < y |
|>=	| Greater than or equal to	| x >= y |
|<=	| Less than or equal to	| x <= y |


If statements are defined with an evaluation followed by a colon, then indented blocks of code:
```python
if True:
  print("this statement will always print")
```

## If / Else / Elif
if and else work as expected, and the python equivalent to javascripts version of `else if` is just `elif`
```python
a = 1
b = 2

if a > b:
    print("a is greater")
elif b > a:
    print("b is greater")
else:
    print("a and b are equal")

# b is greater
```
