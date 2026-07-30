# Day 12 – Python Modules & Packages

## 1. What is a Module?

A module is a Python file (`.py`) that contains functions, variables, or other Python code that can be reused in another Python program.

Example:

calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

We can use this module in another file:

import calculator

print(calculator.add(10, 5))

Output:
15


## 2. Why Do We Use Modules?

Modules help us:

- Reuse code
- Avoid writing the same code repeatedly
- Divide large programs into smaller files
- Keep code organized
- Make programs easier to maintain


## 3. Importing a Module

To use another module:

import module_name

Example:

import math

print(math.sqrt(25))

Output:
5.0


## 4. Importing Specific Functions

Instead of importing the entire module:

from module_name import function_name

Example:

from math import sqrt

print(sqrt(25))

Output:
5.0


## 5. Importing Multiple Functions

We can import multiple functions:

from calculator import add, subtract

print(add(10, 5))
print(subtract(10, 5))


## 6. Using Aliases with `as`

An alias gives a module a shorter name.

Example:

import calculator as calc

print(calc.add(10, 20))

Output:
30

Common examples used in Python:

import numpy as np
import pandas as pd


## 7. Built-in Modules

Python provides many built-in modules.

Examples:

- math
- random
- datetime


### math Module

Used for mathematical operations.

Example:

import math

print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)


### random Module

Used to generate random values.

Example:

import random

number = random.randint(1, 10)

print(number)

Another useful function:

random.choice()

Example:

fruits = ["Apple", "Mango", "Banana"]

print(random.choice(fruits))


### datetime Module

Used to work with dates and time.

Example:

import datetime

current_time = datetime.datetime.now()

print(current_time)


## 8. Creating Our Own Module

File: math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b


File: main.py

import math_operations

print(math_operations.add(10, 5))
print(math_operations.subtract(10, 5))
print(math_operations.multiply(10, 5))
print(math_operations.divide(10, 5))


## 9. What is a Package?

A package is a folder containing related Python modules.

Simple difference:

Module = One Python (.py) file

Package = Folder containing Python modules


Example:

calculator/
│
├── __init__.py
├── basic.py
└── advanced.py


Here:

calculator = Package

basic.py = Module

advanced.py = Module


## 10. __init__.py

`__init__.py` is commonly used inside a Python package.

Example:

calculator/
│
├── __init__.py
├── basic.py
└── advanced.py


## 11. Importing From a Package

Suppose basic.py contains:

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


We can import it using:

from calculator.basic import add, subtract

print(add(10, 5))
print(subtract(10, 5))


## 12. External Packages

Python also has packages that can be installed separately.

We commonly use pip to install them.

Example:

pip install numpy

Then:

import numpy


## 13. Module vs Package

| Module | Package |
|--------|---------|
| Single Python file | Folder containing modules |
| Ends with .py | Contains related Python files |
| Used to organize functions/code | Used to organize multiple modules |

Example:

calculator.py → Module

calculator/ → Package


## 14. Important Import Syntax

Import entire module:

import calculator

Import one function:

from calculator import add

Import multiple functions:

from calculator import add, subtract

Use alias:

import calculator as calc

Import from package:

from calculator.basic import add


## 15. Key Concepts Learned

- Modules
- Packages
- import
- from ... import
- Aliases using `as`
- Built-in modules
- Custom modules
- External packages
- __init__.py
- pip


## 16. Built-in Modules Practiced

- math
- random
- datetime


## 17. Why Modules Are Important

Instead of writing a large program in one file:

main.py
    1000+ lines

We can divide it into:

project/
│
├── main.py
├── calculator.py
├── database.py
├── utilities.py
└── commands.py

This makes the program:

- Cleaner
- Easier to understand
- Easier to debug
- Easier to maintain
- More reusable


## 18. Day 12 Projects

- Custom Math Module
- Calculator Package
- Modular Calculator
- Temperature Converter Module


## 19. Most Important Things to Remember

1. A module is a Python file.

2. A package organizes multiple modules.

3. `import` allows us to reuse code from another module.

4. `from module import function` imports a specific function.

5. `as` creates an alias.

6. Python provides built-in modules such as math, random, and datetime.

7. We can create our own modules.

8. pip is commonly used to install external Python packages.


## Reflection

Today I learned how to divide Python programs into multiple files using modules and packages.

Modules allow me to reuse functions instead of writing the same code repeatedly.

Packages help organize multiple related modules, which becomes important when building larger Python applications.