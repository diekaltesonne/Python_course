# asyncio, Hello World
import asyncio

@asyncio.coroutine
def hello_world():
    while True:
        print("hello_world!")
        yield from asyncio.sleep(1.0)
