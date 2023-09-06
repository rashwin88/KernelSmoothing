import numpy as np
import math

def create_normal_perturbations(point_list, variance=1):
    """
    Creates a normal perturbation given a set points. By perturbation we mean a small random change to the
    value of each item in the list so that some noise is introduced to the orderly output of an underlying function.
    Here we generate a normal perturbation , which means that each point is disturbed in such a way that
    it is replaced by a value picked randonly from a normal distribution centered at that point with the
    specified variance.

    Arguments:
    ----------
    :param point_list: The input point list
    :param variance: The variance to be used in the normal distribution that is used in random sampling.
    :return: A list of perturbed values.
    """

    return [np.random.normal(point, variance) for point in point_list]