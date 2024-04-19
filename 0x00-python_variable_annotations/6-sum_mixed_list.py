#!/usr/bin/env python3

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of integers and floats in the given mixed list.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and floats.

    Returns:
        float: The sum of all integers and floats in the input list.
    """
    total_sum: float = 0.0  # Initialize total sum as a float

    for num in mxd_lst:
        total_sum += num

    return total_sum
