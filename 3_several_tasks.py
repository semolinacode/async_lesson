import asyncio
import random
import time


async def foo(param):
    await asyncio.sleep(random.randint(1, 3))
    print(f'start foo with param {param}')
    await asyncio.sleep(random.randint(1, 3))
    print(f'end foo with param {param}')


async def main1():
    t1 = time.time()
    await asyncio.wait([
        asyncio.create_task(foo(1)),
        asyncio.create_task(foo(2)),
        asyncio.create_task(foo(3)),
    ])
    t2 = time.time()
    print(t2 - t1)


async def main2():
    t1 = time.time()
    await asyncio.gather(
        asyncio.create_task(foo(1)),
        asyncio.create_task(foo(2)),
        asyncio.create_task(foo(3)),
    )
    t2 = time.time()
    print(t2 - t1)


if __name__ == '__main__':
    asyncio.run(main2())
