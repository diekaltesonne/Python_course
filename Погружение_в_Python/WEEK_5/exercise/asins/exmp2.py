import asyncio
async def slow_operation(future):
    await asyncio.sleep(1)
    future.set_result("future is done")
