# Classes

## Declaring classed, and instances
A class is declared using the `class` keyword followed by a class name (class names are typically capitalised). A class must contain at least one line of code inside its block, otherwise the code will error when you attempt to create an instance of it. (But the code block could just be a string as a work-around)

Once a class is declared, instances can be created by invoking the class name (syntactically similar to invoking a function), thereby creating an `object` from that class:

```python
class Dog():
  ""
dog1 = Dog()
print(Dog) # <class '__main__.Dog'>
print(dog1) # <__main__.Dog object at 0x103c065f8>
```

## Class Variables and Instance Variables
A class variable is a value that belongs to the class, and is consistent across all instances of that class. These are declared in the class declaration, or assigned to the class.

An instance variable, by contrast, is a value that can be specific to individual instances of that class, and can vary from instance to instance.

```python
class Car:
    info = "Has wheels and drives places"

car1 = Car()
car1.color = "red"
car2 = Car()
car2.color = "blue"

print(car1.color) # red
print(car2.color) # blue

print(car1.info) # Has wheels and drives places
print(Car.info) # Has wheels and drives places
```
