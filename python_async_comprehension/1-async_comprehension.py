#!/usr/bin/env python3
"""Task 1. Async Comprehensions"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random number
    """
    return [number async for number in async_generator()]
