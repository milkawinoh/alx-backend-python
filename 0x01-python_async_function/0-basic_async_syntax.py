#!/usr/bin/env python3
"""Asynchronous Task Module.

This module provides functions for asynchronous tasks using asyncio.
"""

import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """Asynchronously wait for a random duration.

    This coroutine function waits for a random duration between 0 and
    `max_delay` seconds using asyncio.sleep.

    Args:
        max_delay (float, optional): The maximum delay
        in seconds (default is 10).

    Returns:
        float: The actual delay waited before returning.

    Example:
        >>> await wait_random(5)
        2.345  # This delay is an example and will vary.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
