"""
Python async await
"""

import asyncio



async def start():
    """
    Start the program
    """
    print("Started")
    await asyncio.sleep(2)
    print("Terminated. ")


async def running():
    """
    Executing the program
    """
    print("Running...")

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

    await asyncio.gather(start(), running())

    await async_func()  # this will do nothing because coroutine object is created but not awaited
    await async_func()



asyncio.run(main())
