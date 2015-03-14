#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK7 warmup task_04 - testing for loops."""


def process_data(data):
    """Returns a tuple with the total sum and the average of the data.

    Args:
        data (mixed): A list or tuple of numbers.
    Returns:
        tuple: Containing the data points total sum of and the average of
        the data with a floating point precision.

    Example:
    >>> process_data([1, 5, 7, 8])
    (21, 5.25)

    >>> process_data([10, 15, 25, 46])
    (96, 24.0)

    """
    mysum = sum(data)
    myavg = mysum / float(len(data))
    return (mysum, myavg)
