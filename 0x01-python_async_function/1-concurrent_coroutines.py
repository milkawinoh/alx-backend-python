#!/usr/bin/env python3
"""Asynchronous Multiple Task Execution Module.

This module provides functions for executing multiple asynchronous tasks
simultaneously using asyncio.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines concurrently and collect results.

    This coroutine function creates `n` instances of
    the `wait_random` coroutine with a specified maximum delay
    It then uses `asyncio.as_completed`
    to await the completion of these coroutines and collects the results.

    Args:
        n (int): The number of coroutines to execute concurrently.
        max_delay (int): The maximum delay in seconds for each coroutine.

    Returns:
        List[float]: A list of floats representing the delays
          waited by each coroutine.

    Example:
        >>> delays = await wait_n(3, 5)
        >>> print(delays)
        [2.3, 4.8, 1.2]
    """
    delays: List[float] = []
    all_delays: List[float] = []

    # Start `n` instances of the `wait_random` coroutine
    for i in range(n):
        delays.append(wait_random(max_delay))

    # Wait for coroutines to complete using asyncio.as_completed
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)

    return all_delays
