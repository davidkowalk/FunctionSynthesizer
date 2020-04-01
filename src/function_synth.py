from numpy.linalg import solve as solve_linalg
from numpy import empty as new_array
from numpy import array

def solve(points: array, suspend_tests = False):

    y_size, x_size = points.shape

    if not suspend_tests:

        if not x_size == 2:
            raise ValueError("Invalid Format!\nProvide points in the following format:\narray([\n    [x1, y1],\n    [x2, y2],\n    ...\n    [xn, yn]\n])")

        if not len(points) >= 2:
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

    return coefficients




def to_str(polynomial: array):
    pass
