# Function Synthesizer

This API provides an easy way to generate a polynomial from a set of n points.

**Contents**
- Importing the API
- Dependencies
- Functions

## Importing the API
To import this API, first clone it from [GitHub](http://github.com/DapfiDuck/FunctionSynthesizer) with

```
git clone https://github.com/davidkowalk/FunctionSynthesizer.git
```
or download it from the [GitHub page](http://github.com/DapfiDuck/FunctionSynthesizer).
Then copy the file ``src/function_synth.py`` into the source folder of your project and import it with:
```
import function_synth as synth
```

## Dependencies
- Python 2.7
- numpy

## Functions

### solve()

Solves for the coefficients of a polynomial function through a set a points.

|   Parameters  |     Type    |Description|Required|
|---------------|-------------|-----------|--------|
| points        | numpy.array | An array of the points the function should run through. (2D)| yes |
| suspend_tests | Boolean     | Whether the imputs should be checked. **Default: False**    | no  |

The array of points must have the format 2*n:
```
points = numpy.array([
  [x1, y1],
  [x2, y2],
  ...
  [xn, yn]
])
```

Example:

```
points = array([
  [0, 0],
  [4, 2],
  [8, 4],
  [12, 6],
  [18, 8],
  [22, 0]
])

coefficients = synth.solve(points)

print(coefficients)
```

Output:
```
[-3.30687831e-05  1.32275132e-03 -1.85185185e-02  1.05820106e-01  2.96825397e-01  0.00000000e+00]
```

### to_str()

Takes an array with coefficients and generates a string expression of the polynomial equation.

|   Parameters  |     Type    |Description|Required|
|---------------|-------------|-----------|--------|
| coefficients  | numpy.array or List | An array of the functions coefficients.| yes |

Example:
```
coefficients = [ -0.05, 0.5, 10 ]
eqn = synth.to_str(coefficients)

print(eqn)
```
Output:
```
f(x) = -0.05 x² + 0.5 x + 10
```
