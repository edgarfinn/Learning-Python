## Functions

The `def` keyword is used to define a function, the first line is used to name the function and list its arguments in parentheses. This first line is distinguished from the code block with a colon, and by indenting the code block.

The first few lines of a function's code block can be used to add a comment describing the behaviour of the function. This is known as a docstring. These always occur as the first statement in a module, function, class, or method definition, and they become the `__doc__` special attribute of that object.

Its common practise to write doc strings
```python
def helloWorld(name):
  '''Prints a greeting to the name provided'''
  print('Hello', name)


helloWorld('John')
# Hello John

print(helloWorld.__doc__)
# Prints a greeting to the name provided
```

The `return` keyword is used to define the value returned from a function's invocation:
```python
def addNums(num1, num2):
  total = num1 + num2
  return total

twoPlusOne = addNums(2, 1)
print(twoPlusOne)

#3
```
The return statement concludes the code block of a function, so no code after the return statement will be evaluated.


### Arguments
Unless specified otherwise, a functions arguments are evaluated in the same order as they are defined:

But you can also explicitly name the arguments that you're passing in according to the names given in the function definition, allowing you to pass these in any order:

```python
def helloNames(firstName, secondName):
  print('Hello', firstName, secondName)

helloNames('john', 'smith')
# Hello john smith

helloNames('smith', 'john')
# Hello smith john

helloNames(secondName='smith', firstName='john')
# Hello john smith
```
### Default values
You can define default values for function arguments, which will be used if no such argument is passed in:

```python
def helloNames(firstName="John", secondName="Smith"):
  print('Hello', firstName, secondName)

helloNames()
# Hello John Smith
```

**Arbitrary argument lists:**
You can specify that a function can receive a variable number of arguments as the final (or only) argument being passed in, denoting these with an *asterisk. This arbitrary list of arguments will then be treated inside the function as a tuple:

```python
def greetings(first, second, *allTheRest):
  print('Hello', first)
  print('Hello', second)
  print('and hello too all of', *allTheRest)

  greetings("John", "Ellie", "Simon", "Cassie", "Rachel")
  # Hello John
  # Hello Ellie
  # and hello too all of Simon Cassie Rachel
```
```python
def addAllNumbers(*anyAmountOfNumbers):
    print(anyAmountOfNumbers)
    print('added = ', sum(anyAmountOfNumbers))

addAllNumbers(1, 2)
addAllNumbers(1, 2, 3)
# (1, 2)
# added =  3
# (1, 2, 3)
# added =  6
```

### Function Annotations:

You can annotate the return value of a function using an arrow at the end of the first line. This is called an annotation, and is similar to the docstring in the respect that it does not affect the performance or behaviour of the function, but can be accessed and used by other functions / libraries by accessing the `function.__annotations__` variable. As you'll see from the `-> int` annotation and returned string below, the annotation has no direct effect on the functions behaviour / requirements.

```python
def helloWorld() -> int:
  return "Hello world"

print(helloWorld())
print(helloWorld.__annotations__)
# Hello world
# {'return': <class 'int'>}
```
