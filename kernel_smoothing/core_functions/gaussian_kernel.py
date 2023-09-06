import numpy as np
import math
def gaussian_kernal_1d(x: float, centering_point: float, window_size: float = 1):
    """
    Computes the kernel value at a specified point x in relation to a point x_i which is the centering point.
    the window size or bandwidth will have to be specified. This is ofcourse a 1d gaussian kernel and not n-dimensional
    and hence can be used in smoothing 2d curves.

    The kernel is of the form f(x,x_i) = exp(-(x-x_i)^2/2b^2)
    Arguments:
    ----------
    :param x: The point at which the estimation is to be done.
    :param centering_point: Basically x_i in the kernel function.
    :param window_size: The bandwidth or variance parameter.
    :return:
    """

    return math.exp(-1 * (x-centering_point)**2 / (2 * window_size**2))
