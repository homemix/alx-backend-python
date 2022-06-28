#!/usr/bin/env python3
"""
:returns a random number between 0 and 10
"""
import asyncio
import random


async def async_generator() -> float:
    """
    :returns a random number between 0 and 10
    :return:
    :rtype:
    """
    number = random.uniform(0, 10)
    for _ in range(0, 10):
        yield number
        await asyncio.sleep(1)
        number = random.uniform(0, 10)
    print(number)
