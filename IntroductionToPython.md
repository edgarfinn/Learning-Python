# Quick Introduction to Python

### Overview
Python is an [interpreted](https://en.wikipedia.org/wiki/Interpreted_language#:~:text=An%20interpreted%20language%20is%20a,program%20into%20machine%2Dlanguage%20instructions.), [dynamically typed](https://en.wikipedia.org/wiki/Dynamic_programming_language), [garbage-collected](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)), high-level, general-purpose programming language. Its design philosophy emphasises code readability, notable for its use of significant whitespace. It supports multiple programming paradigms, including [structured](https://en.wikipedia.org/wiki/Structured_programming) (particularly [procedural](https://en.wikipedia.org/wiki/Procedural_programming)), [object-oriented](https://en.wikipedia.org/wiki/Object-oriented_programming), and [functional](https://en.wikipedia.org/wiki/Functional_programming) programming.

Python is a versatile language, which lends itself to a range of applications including Web & Internet Development, Database Access, Desktop GUIs, Scientific & Numeric computing (including Data Analysis), Network Programming and Software and Game development.

Python files are marked with the `.py` file extension.

### Grammar
- Python is case sensitive.
- The end of a line marks the end of a statement (ie no semicolon required).
- Blocks of code are grouped using indentation (as opposed to, say, curly braces).
- Comments can be denoted either as single-lines, using the `#` symbol (extending to the end of the line), or across multiple lines wrapping the comment block with three quotation marks:
```Python
 # This is a single-line commend

 '''
 This is a multi-
 line comment
 '''
```


### Imports, Command-line and `len()`


Python modules can either be run directly (ie network-request / command line), OR imported and run by other modules as part of a larger program. When a file is run directly, the special variable `__name__` is set to `__main__`.

Defining the `main` function is a necessity to start the execution of the program. It acts as the ["entry-point"](https://en.wikipedia.org/wiki/Entry_point) for any program. If a module is being run directly, the module needs to execute its main function, so its common to see the following boilerplate in entry-point files:

```Python
if __name__ == '__main__':
  main()
```

This essentially calls the main function when the module is run directly.

The `sys` module is one of the many utilities included in the [Python Standard Library](https://docs.python.org/3/library/), which is included as part of the Python installation package, and can be used to access arguments passed from the command-line into a Python program.

```Python
#helloWorld.py
import sys

def main():
    print sys.argv
    argumentsLength = len(sys.argv)
    print 'argumentLength:', argumentsLength
    if argumentsLength > 1:
        print 'first argument:', sys.argv[1]

if __name__ == '__main__':
    main()
```

 In general, `len()` can tell you how long a string is, the number of elements in lists and tuples (another array-like data structure), and the number of key-value pairs in a dictionary.

### Defining Functions
