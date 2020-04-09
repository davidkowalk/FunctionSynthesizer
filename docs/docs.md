# Function Synthesizer

This API provides an easy way to generate a polynomial interpolation from a set of n points.

**Contents**
- Importing the API
- Dependencies
- Functions

## Importing the API
To import this API, first clone it from [GitHub](http://github.com/davidkowalk/FunctionSynthesizer) with

```bash
git clone https://github.com/davidkowalk/FunctionSynthesizer.git
```
or download it from the [GitHub page](http://github.com/DapfiDuck/FunctionSynthesizer).
Then copy the file ``src/function_synth.py`` into the source folder of your project.

Alternatively you can use pip to import the API into your python-environment from the unpacked download. Make sure to link to the folder with ``setup.py``:
```bash
pip install ~/Path/To/Repo/Folder/
```

Now import the API with:
```python
import function_synth as fs
```

## Dependencies
- Python 3.6
- numpy

## Functions

**Functions**

|            Name             | Description |
|-----------------------------|-------------|
| [solve](#solve)             | Solves for the coefficients of a polynomial function through a set a points.
| [solve_mixed](#solve_mixed) | Solves for the coefficients of a polynomial function through a set a points on the nth derivative
| [to_str](#to_str)           | Takes an array with coefficients and generates a string expression of the polynomial equation.
| [calculate](#calculate)     | Takes in a List of coefficients and an x-value to calculate f(x).

### solve()

Solves for the coefficients of a polynomial function through a set a points.

|   Parameters  |     Type    |Description|Required|
|---------------|-------------|-----------|--------|
| points        | numpy.array | An array of the points the function should run through. (2D)            | yes |
| suspend_tests | Boolean     | Whether the imputs should be passed without checked. **Default: False** | no  |
| steps         | Boolean     | When true will return a tuple (coefficients, matrix. solutions).        | no  |

The array of points must have the format 2*n:
```python
points = numpy.array([
  [x1, y1],
  [x2, y2],
  ...
  [xn, yn]
])
```

**Example:**

```python
points = array([
  [0, 0],
  [4, 2],
  [8, 4],
  [12, 6],
  [18, 8],
  [22, 0]
])

coefficients = fs.solve(points)

print(coefficients)
```

Output:
```python
numpy.array([-3.30687831e-05  1.32275132e-03 -1.85185185e-02  1.05820106e-01  2.96825397e-01  0.00000000e+00])
```

### solve_mixed()

Solves for the coefficients of a polynomial function through a set a points.

|   Parameters  |     Type    |Description|Required|
|---------------|-------------|-----------|--------|
| points        | numpy.array | An array of the points the function should run through. (2D)            | yes |
| suspend_tests | Boolean     | Whether the imputs should be passed without checked. **Default: False** | no  |
| steps         | Boolean     | When true will return a tuple (coefficients, matrix. solutions).        | no  |

The array of points must have the format 3*n:
```python
points = numpy.array([
  [x1, y1, k1],
  [x2, y2, k2],
  ...
  [xn, yn, kn]
])
```
k defines the k-th derivative the point runs through.

**Example:**

```python
points = numpy.array([
[2,1,0],
[8,1,0],
[1,2,1]
])

c = fs.solve_mixed(points)

print(coefficients)
```

Output:
```python
numpy.array([-0.25,  2.5 , -3.  ])
```

### to_str()

Takes an array with coefficients and generates a string expression of the polynomial equation.

|   Parameters  |     Type    |Description|Required|
|---------------|-------------|-----------|--------|
| coefficients  | numpy.array or List | An array of the functions coefficients.| yes |

**Example:**
```python
coefficients = [ -0.05, 0.5, 10 ]
eqn = fs.to_str(coefficients)

print(eqn)
```
Output:
```
f(x) = -0.05 x² + 0.5 x + 10
```

### calculate()

Takes in a List of coefficients and an x-value to calculate f(x) where ``f(x) = SUMM [k=0 to n]  (a_k*x^k)``

|   Parameters  |     Type    |Description|Required|
|---------------|-------------|-----------|--------|
| coefficients  | numpy.array or List | An array of the functions coefficients.| yes |
| x             | float or int        | The point to be calculated | yes |

**Example:**

```python
coefficients = [ -0.05, 0.5, 10 ]
x = 3

y = fs.calculate(coefficients, x)
print(y)
```
Output:
```
10
```
