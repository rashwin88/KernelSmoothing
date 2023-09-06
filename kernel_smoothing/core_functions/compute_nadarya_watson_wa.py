import numpy as np
import math
from kernel_smoothing.core_functions import gaussian_kernel as gk

def compute_nadarya_watson_wa(x:float, training_points: list, bandwidth: float = 1):
    """
    Computes the Nadarya-Watson weighted average to estimate the value of a function at x given a set of training points.

    Arguments:
    ----------
    :param x: The point at which the weighted average is to be computed.
    :param training_points: The training points to be used in the computation. A list of lists constaining x and y as two lists
    :param bandwidth: The bandwith of the gaussian kernel
    :return:
    """

    # first compute the kernel values at the given points
    kernel_values = [gk.gaussian_kernal_1d(x, xi, bandwidth) for xi in training_points[0]]

    # then compute the product of each kernel value with the value of the function
    kernel_products = [kv * yi for kv,yi in zip(kernel_values,training_points[1])]

    # return the weighted average
    return np.sum(kernel_products) / np.sum(kernel_values)