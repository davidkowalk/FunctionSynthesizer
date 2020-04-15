from numpy.linalg import solve as solve_linalg
from numpy import empty as new_array
from numpy import array


def __derive__(a, power, n):
    """
    Takes a*x^power and the derivation number.
    Returns a numpy array of the coefficient and the power: a*x^b -> array([a, b])"""

    if n < 0:
        raise ValueError("Can't integrate.")
    elif n == 0:
        return array([a, power])

    a *= power

    if power > 0:
        power -= 1

    n -= 1

    if n <= 0 or (a == 0 and power == 0):
        return array([a, power])
    else:
        return __derive__(a, power, n)


def solve_mixed(points: array, suspend_tests = False, steps = False):

    """
    Takes a set of points with a derivative assigned to each and generates the coefficients of a polynomial interpolation where each point lies on it's respective derivative.
    The 0th derivative is f(x) while the first derivative is f'(x) or df/dx and so forth.


    Example
    -------
    >>> points = numpy.array([
    >>> [2,1,0], # On the function f(x)
    >>> [8,1,0], # On the function f(x)
    >>> [1,2,1]  # On the derivative f'(x)
    >>> ])

    >>> fs.solve_mixed(points)

    array([-0.25,  2.5 , -3.  ])
    """

    y_size, x_size = points.shape

    if not suspend_tests:

        if not x_size == 3:
            raise ValueError("Invalid Format!\nProvide points in the following format:\narray([\n    [x1, y1, i1],\n    [x2, y2, i2],\n    ...\n    [xn, yn, in]\n])")

        if not y_size >= 2:
            raise ValueError("Invalid Input!\nMust provide at least 2 points.")

    matrix = new_array((y_size, y_size))
    solutions = new_array(y_size)

    max_pol = y_size-1

    for index in range(len(points)):
        point = points[index]
        pol = max_pol

        row = []

        while pol >= 0:

            #print(f"d-{point[2]}: x^{pol}")
            a, applied_power = __derive__(1, pol, point[2]) #Get coefficient and power for nth derivative
            #print(f"d-{point[2]}: {a}*x^{applied_power}\n")

            row.append(a*point[0]**applied_power)
            pol-=1

        matrix[index] = row
        solutions[index] = point[1]

    coefficients = solve_linalg(matrix, solutions)

    if steps:
        return (coefficients, matrix, solutions)
    else:
        return coefficients

def solve(points: array, suspend_tests = False, steps = False):

    """
    Takes a set of points and generates the coefficients of a polynomial interpolation through all of the points.


    Example
    -------
    >>> points = numpy.array([
    >>> [1,1],
    >>> [5,5],
    >>> [-1,2]
    >>> ])

    >>> fs.solve(points)

    array([ 0.25, -0.5 ,  1.25])
    """

    y_size, x_size = points.shape

    if not suspend_tests:

        if not x_size == 2:
            raise ValueError("Invalid Format!\nProvide points in the following format:\narray([\n    [x1, y1],\n    [x2, y2],\n    ...\n    [xn, yn]\n])")

        if not y_size >= 2:
            raise ValueError("Invalid Input!\nMust provide at least 2 points.")

    matrix = new_array((y_size, y_size))
    solutions = new_array(y_size)

    max_pol = y_size-1

    for index in range(len(points)):
        point = points[index]
        pol = max_pol

        row = []

        while pol >= 0:
            row.append(point[0]**pol)
            pol-=1

        matrix[index] = row
        solutions[index] = point[1]

    coefficients = solve_linalg(matrix, solutions)

    if steps:
        return (coefficients, matrix, solutions)
    else:
        return coefficients


def to_str(polynomial: array):

    """
    Takes a numpy.array or List of coefficients and renders the corresponding function.

    Example
    -------

    >>> coefficients = numpy.array([ 0.25, -0.5 ,  1.25])
    >>> print(fs.to_str(coefficients))

    f(x) = 0.25*x^2 + -0.5*x^1 + 1.25
    """

    function = "f(x) = "

    pow = len(polynomial)-1

    for coefficient in polynomial:
        if pow > 0:
            function += f"{coefficient}*x^{pow} + "
        else:
            function += f"{coefficient}"

        pow -= 1

    return function

def calculate(polynomial: array, x: float):
    """
    Takes a numpy.array or list of the coefficients and a point x and calculates the corresponding f(x).
    """

    pow = len(polynomial)-1
    f = 0

    for coefficient in polynomial:
        f += coefficient*x**pow
        pow -= 1

    return f


def read(path, x_col, y_col, title=False, delimiter=",", quotechar="\""):
    import csv

    sheet = []

    with open(path) as file:
        reader = csv.DictReader(file, delimiter=delimiter, quotechar=quotechar)

        for row in reader:
            sheet.append([float(row[x_col]), float(row[y_col])])

    return array(sheet)
