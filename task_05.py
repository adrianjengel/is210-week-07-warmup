#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK7 warmup task_05 - mutability difference"""


def flip_keys(to_flip):
    """ A function that reverses the input list.

    Args:
        data (mixed): A list of numbers or letters.
    Returns:
        data (mixed): A list of numbers of letters in reverse.

    Examples:
        >>> print flip_keys([(1, 2, 3), 'abc'])
        [(3, 2, 1), 'cba']

        >>> print flip_keys(['Good Day', (12, 34, 56)])
        ['yaD dooG', (56, 34, 12)]
    """

    counter = 0
    for values in to_flip:
        to_flip[counter] = values[::-1]
        counter += 1
    return to_flip
