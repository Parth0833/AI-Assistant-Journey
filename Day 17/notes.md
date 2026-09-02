# Day 17 – Lambda Functions, Iterators & Generators

## Lambda Functions

A lambda function is a small anonymous function.

Syntax:

lambda arguments: expression

Example:

square = lambda x: x * x

## map()

map() applies a function to every element of an iterable.

Example:

result = map(lambda x: x * 2, numbers)

## filter()

filter() selects elements based on a condition.

Example:

result = filter(lambda x: x % 2 == 0, numbers)

## Iterators

An iterator allows values to be accessed one at a time.

iter() creates an iterator.

next() returns the next value.

## Generators

A generator produces values one at a time using yield.

Example:

def numbers():
    yield 1
    yield 2
    yield 3

## return vs yield

return:
- Returns a value
- Ends the function

yield:
- Produces values one at a time
- Allows the function to continue from where it stopped

## Key Learning

Generators are useful when working with large amounts of data because they do not need to store all values in memory at once.

## Important Concepts

Lambda → Small anonymous function
map() → Transform data
filter() → Select data
iter() → Create iterator
next() → Get next value
yield → Produce generator values