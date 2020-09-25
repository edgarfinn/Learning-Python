# Quick Introduction to Python

### Overview
Python is an [interpreted](https://en.wikipedia.org/wiki/Interpreted_language#:~:text=An%20interpreted%20language%20is%20a,program%20into%20machine%2Dlanguage%20instructions.), [dynamically typed](https://en.wikipedia.org/wiki/Dynamic_programming_language), [garbage-collected](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)), high-level, general-purpose programming language. Its design philosophy emphasises code readability, notable for its use of significant whitespace. It supports multiple multiple programming paradigms, including [structured](https://en.wikipedia.org/wiki/Structured_programming), (particularly [procedural](https://en.wikipedia.org/wiki/Procedural_programming)), [object-oriented](https://en.wikipedia.org/wiki/Object-oriented_programming), and [functional](https://en.wikipedia.org/wiki/Functional_programming) programming.

Python is a versatile language, which lends itself to a range of applications including Web & Internet Development, Database Access, Desktop GUIs, Scientific & Numeric (including Data Analysis), Network Programming and Software and Game development.

Python files are marked with the `.py` file extension.

### Grammar
A few things to note about Python's grammar. It is:
- Python is case sensitive.
- The end of a line marks the end of a statement. (No semicolon required).
- Blocks of code are grouped using indentation (as opposed to, say, curly braces).
- Comments can be denoted either as single-lines, using the `#` symbol (extending to the end of the line), or across multiple lines, using three quotation marks:
```Python
 # This is a single-line commend

 '''
 This is a multi-
 line comment
 '''
```


### `__main__`


Python modules (ie files) can either be run directly (ie network-request / command line), OR imported and run by other modules as part of a larger program. When a file is run directly, the special variable `__name__` is set to `__main__`.

Defining the `main` function is a necessity to start the execution of the program. It acts as the point for any program. If a module is being run directly, the module needs to execute its main function, so its common to see the following boilerplate in ["entry-point"](https://en.wikipedia.org/wiki/Entry_point) files:

```Python
if __name__ == '__main__':
  main()
```

This essentially calls the main function when the module is run directly.

```Python
#helloworld.py
import sys

def main():
  print sys.argv
```

### Arguments from the command line

### Defining Functions