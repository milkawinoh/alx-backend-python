#!/usr/bin/env python3

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of float numbers in the given list.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of all float numbers in the input list.
    """
    total_sum: float = 0.0  # Initialize total sum as a float

    for num in input_list:
        total_sum += num

    return total_sum