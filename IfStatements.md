# If Statements, Comparisons and Boolean basics

Booleans are capitalised keywords.
```python
True
False
```
## If / Else / Elif

If statements are defined with an evaluation followed by a colon, then indented blocks of code:
```python
if True:
  print("this statement will always print")
```

`if` and `else` work as expected, and the python equivalent to javascripts version of `else if` is just `elif`
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


You can chain operators to identify numbers that fall within a range:

```python
a = 6
if 7>= a >=5:
  print("between five and seven")
```

You can further specify if-conditions using the `and` and `or` keywords (similar to `&&` and `||` in javascript) by marking the start of a separate condition which is additionally or alternatively (respectively) evaluated.

```python
a = 8
b = 7

if 3 <= a <= 9 and a % 2 == 0:
    print("a is between 3 and 9 and even")

if 3 <= b <= 9 and b % 2 == 0:
    print("b is between 3 and 9 and even")

# a is between 3 and 9 and even
```
