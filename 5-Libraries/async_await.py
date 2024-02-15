"""
async await functions
"""

import asyncio


async def async_func():
    """
    async function
    """
    print("Velotio ...")
    await asyncio.sleep(5)
    print("... Technologies!")


async def main():
    """
    main function
    """
    async_func()  # this will do nothing because coroutine object is created but not awaited
    await async_func()


asyncio.run(main())
