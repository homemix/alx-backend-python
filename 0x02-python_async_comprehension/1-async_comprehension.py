#!/usr/bin/env python3
import asyncio
from typing import List

"""
:returns async generator for a random number between 0 and 10
"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    :returns async generator for a random number between 0 and 10
    :return:
    :rtype:
    """
    return [i async for i in async_generator()]
