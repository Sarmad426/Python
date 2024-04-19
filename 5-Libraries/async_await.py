"""
Python async await
"""

import asyncio


<<<<<<< HEAD
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
=======
async def async_func():
    """
    async function
    """
    print("Velotio ...")
    await asyncio.sleep(5)
    print("... Technologies!")
>>>>>>> 24b81532c936e2c6bada4d8e97c826cb6f4263aa


async def main():
    """
    main function
    """
<<<<<<< HEAD
    await asyncio.gather(start(), running())
=======
    async_func()  # this will do nothing because coroutine object is created but not awaited
    await async_func()
>>>>>>> 24b81532c936e2c6bada4d8e97c826cb6f4263aa


asyncio.run(main())
