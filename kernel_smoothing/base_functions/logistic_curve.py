import math
import numpy as np

def logistic_curve(x_range:list=[-5,5], L:float=1, k:float=1, x0:float=0, interval_length:float=0.01):
    """
    Implements a logistic function which is given by the equation
    f(x) = L / (1 + exp(-k(x-x0)))

    Arguments:
    ----------
    :param x_range: The X-range with in which the function must be computed.
    :param L: The supremum of the values of the function.
    :param k: The logistic growth rate
    :param x0: The x value of the functions midpoint.
    :param interval_length: The interval size used to generate x points for getting the function values
    :return:
    """

    xvals = np.arange(x_range[0], x_range[1], interval_length)
    yvals = [L / (1 + math.exp(-1 * k * (x - x0))) for x in xvals]
    return [[*xvals], yvals]