# FunctionSynthesizer

Takes any number of points in a matrix and returns a polynomial function that runs through all points.

The API prepares the matrix and then runs it through ``numpy.solve_linalg()`` to generate a number of coefficients. It also provides functions to render the function as a string and to calculate f(x) based on it's coefficients and a value x.

## Dependencies

- numpy
- python 2.7 (Early versions untested)

## About

|    Tag   | Value |
|----------|-------|
| Author   | David J. Kowalk
| License  | MIT
| Released | 2020-04-01
