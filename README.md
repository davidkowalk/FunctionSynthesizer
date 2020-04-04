# FunctionSynthesizer

Takes any number of points in a matrix and returns a polynomial function that runs through all points.

The API prepares the matrix and then runs it through ``numpy.solve_linalg()`` to generate a number of coefficients. It also provides functions to render the function as a string and to calculate f(x) based on it's coefficients and a value x.

![Demo Picture](https://github.com/davidkowalk/FunctionSynthesizer/blob/master/docs/Example-6-Points.png?raw=true)

See the docs for a guide.

## Dependencies

- numpy
- python 2.7 (earlier versions untested)

## About

|    Tag   | Value |
|----------|-------|
| Author   | [David J. Kowalk](https://davidkowalk.github.io/)
| License  | MIT
| Released | 2020-04-01
