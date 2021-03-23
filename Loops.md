## Loops

#### For loops
```python
for i in range(x [,y]):
  # do something
```
Where `i` is the current iteration in a total number of x iterations. Or if `y` is also specified, the number of iterations will count from `x` and stop when it reaches `y` (which will not be included).

For example:

```python
for num in range(5):
  print(num)
# 0
# 1
# 2
# 3
# 4

for i in range(5, 8):
  print(i)
# 5
# 6
# 7

games = ["Mario", "Earthworm Jim", "Fifa"]

for game in games:
  print(game)
# Mario
# Earthworm Jim
# Fifa
```

#### While Loops
Very similarly declared to for loops:
```python
age = 3
while age < 10:
  print(age)
  age += 1

#  3
#  4
#  5
#  6
#  7
#  8
#  9
```

#### Infinite loops
Unlike javascript, python will **not always error** in the event of an infinite loop. It seems there may even be some [intentional use-cases](https://www.educba.com/python-infinite-loop/) for infinite loops. So watch out for possible unintentional infinite loops. You wont always get notified by the run time environment if you've accidentally created an infinite loop.

```python
num = 1
while num < 5:
  print("I will run forever")

# I will run forever
# I will run forever
# I will run forever
# etc...
```

#### Break, Continue and Else
- `break` can be used to immediately exit out of a loop. Nothing after the `break` statement will be evaluated or executed.:
```python
for num in range(5):
  print(num)
  if num == 2:
    break
# 0
# 1
# 2
```

- `continue` can be used to skip any remaining code of a given iteration, and continue on from the start of the next iteration. The loop will continue repeating, but any code after the `continue` statement will not be run for the remainder of that particular iteration.

```python
for num in range(5):
  if num % 2 == 0:
    continue
  print(num, 'is odd')
# 1 is odd
# 3 is odd
```

- `else` statements can be used to define a block of code to be run after the loop has completed. The syntax is the same as an if else statement. The `else` statement's code block will only run if the loop is not `break`ed, so `break` statements will short-cirtcuit not only the for / while loop, but also any `else` statement.

```python
for num in range(3):
  print(num)
else:
  print("All done")
#  0
#  1
#  2
#  All done

# NOW WITH A BREAK CLAUSE:
for num in range(3):
  if num == 2:
    break
  print(num)
else:
  print("All done")
# 0
# 1
```
