#!/usr/bin/env python3
"""Asynchronous Runtime Measurement Module.

This module provides a function for measuring the
 runtime of an asynchronous task
using asyncio.
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average runtime per coroutine execution.

    This function measures the average runtime per coroutine
      execution by running
    the `wait_n` coroutine `n` times with a specified
      `max_delay`. It calculates
    the total runtime and returns the average time per coroutine.

    Args:
        n (int): The number of coroutines to execute.
        max_delay (int): The maximum delay in seconds for each coroutine.

    Returns:
        float: The average runtime per coroutine execution.

    Example:
        >>> avg_time = measure_time(5, 3)
        >>> print(avg_time)
        0.7
    """
    start_time = time.time()

    # Execute the `wait_n` coroutine `n` times
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    # Calculate average time per coroutine
    average_time = total_time / n
    return average_time
