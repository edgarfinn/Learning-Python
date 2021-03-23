## Loops

#### For loops
```python
for i in range(x [,y]):
  # do something
```
Where `i` is the current iteration in a total number of x iterations. Or if `y` is also specified, the number of iterations will count from `x` and stop when it reaches `y` (which will not be included).

For example:

```python
for num in range(3):
  print(num)
# 0
# 1
# 2

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

### Infinite loops
Unlike javascript, python will **not always error** in the event of an infinite loop. It seems there may even be some [intentional use-cases](https://www.educba.com/python-infinite-loop/) for infinite loops. So watch out for possible unintentional infinite loops. You wont always get notified by the run time environment if you've accidentally created an infinite loop.
