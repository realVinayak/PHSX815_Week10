from scipy.optimize import fsolve
import math
import numpy as np


def sin_squared(input_value):
    x = input_value[0]
    y = input_value[1]
    value = math.pow(math.sin(x), 2) + math.pow(math.sin(y), 2)
    return [value, value]


def driver():
    root_calculated = (fsolve(sin_squared, np.asarray([3 * math.pi / 4, 3 * math.pi / 4])))
    expected_solution = np.asarray([math.pi, math.pi])
    error_vec = root_calculated - expected_solution
    error = np.linalg.norm(error_vec)
    print('solution found: ', root_calculated)
    print('expected solution: ', expected_solution)
    print('error: ', error)


if __name__ == '__main__':
    driver()
