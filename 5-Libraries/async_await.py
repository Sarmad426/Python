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


async def main():
    """
    main function
    """
    await asyncio.gather(start(), running())


asyncio.run(main())
