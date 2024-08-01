#!/usr/bin/env python3

"""Has sum_list function"""


def sum_list(input_list: list[float]) -> float:
    """
    Adds up floats elements of input_list

    Args:
        input_list (list): a list of floats

    Returns:
        Sum of input_list elements
    """

    sum: float = 0.0

    for number in input_list:
        sum = sum + number

    return sum
