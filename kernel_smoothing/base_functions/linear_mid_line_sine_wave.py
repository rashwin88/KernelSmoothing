import math
import numpy as np

def linear_midline_sine_wave(x_range:list=[-5,5], A:float=10, B:float=10, a:float=0, b:float=1, interval_length:float=0.01):
    """
    A sine wave generator which has a quadratic midline and is defined by the equation
    f(x) = A sin(Bt) + a + bt.

    Arguments:
    ----------
    :param x_range: The X-range with in which the function must be computed.
    :param A: The value of the parameter A
    :param B: The value of the parameter B
    :param a: The value of the parameter a which y-intercept of the sine wave midline
    :param b: The value of the parameter b which controls the slope of the midline.
    :param interval_length: The interval size used to generate x points for getting the function values
    :return:
    """

    xvals = np.arange(x_range[0], x_range[1], interval_length)
    yvals = [A * math.sin(B * x) + (a  + b * x) for x in xvals]
    return [[*xvals], yvals]