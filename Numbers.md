## Basic operators
For numbers and arithmetic, the standard `+`, `-`, `/` and `*` operators work as expected.

There is no `++` operators, but `+=` and `-=` work for incrementing / decrement. Operators `n *= n` and `n /= n` also work as expected; assigning the divided / multiplied result to the existing value to the left.

## Exponents

The `**` operator can be used to multiply exponentially (to the power, eg squared, cubed etc...)

```python
num ** power
```
Where `num` is the number you want to multiply, and power is the power to-which you want to multiply it.

```python
5 ** 2 # = 25 (5 to the power of 2)
5 ** 3 # = 125 (5 to the power of 3)
3.14 ** 2 # = 9.8596
```
## Floor Division
For integer division, if you only want the resulting <ins>integer</ins> (just the "quotient" / the number before the decimal place) from a division; it is most correct to use double forward slashes (eg `6 // 2` would return `3`, `5 // 4` would return `1` etc...).

```python
5 // 2 # = 2
```
...because 2 is the quotient of 2.5, which is the result of 5 / 2.

Division: Python 2 vs Python 3
In python 2, the maths operators wont convert numbers to floats, for example when dividing an odd number by 2, you will only get the quotient back (and not the exact float). Whereas python 3 will happily convert an integer into a float if the result of a division is not a whole number.

For example:
```python
# pyhton2
7 / 2 # = 3 (returns only the quotient)
7.0 / 2 # = 3.5 (because the equation started with a float)

# python3
7 / 2 # = 3.5 (converts int 7/2 into float 3.5)
```

## Rounding numbers
```python
round(num, dec)
```
Where `num` is the number you want to round, and `dec` is the number of decimal places you want to round it to.

```python
round(1.6666667, 2) # = 1.67
round(1.6666667, 0) # = 1.0
round(1.618033, 4) # = 1.618, (only three decimals because the next decimal place would have been a zero)
```

#### Rounding: Python 2 vs Python 3.
- Python 2 will always round floats that sit on the exact half-way (ie `n.5`) to the nearest zero, for example

```python
round(1.5, 0) # = 2.0
round(2.5, 0) # = 3.0
```
...rounding the float to the nearest next biggest decimal place.

- Python 3 however, has been updated to reduce rounding bias by always rounding to the nearest EVEN NUMBER.


```python
round(1.5, 0) # = 2.0
round(2.5, 0) # = 2.0
```

#### Converting numbers (eg decimals / floats) to integers `int()`
The `int()` function can be used to convert non-integer numbers to integers (and therefore round numbers), but beware `int()` method will always round numbers <ins>down</ins> by simply removing any decimal places.

```python
round(2.9, 0) # = 3.0
int(2.9) # = 2
````

#### Converting integers to decimals / floats
Similarly, you can convert integers to floats using the `float()` method:
```python
num = 78.5
num # 78.5
num = int(num)
num # 78
num = float(num)
num # 78.0
```

## Incrementing / Decrementing
Similar to Javascript, numbers can be incremented and decremented using `n += n` and `n -= n`,
