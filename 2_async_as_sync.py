import asyncio
import random
import time


async def foo(param):
    await asyncio.sleep(random.randint(1, 3))
    print(f'start foo with param {param}')
    await asyncio.sleep(random.randint(1, 3))
    print(f'end foo with param {param}')


async def main():
    t1 = time.time()
    await foo(1)
    await foo(2)
    await foo(3)
    t2 = time.time()
    print(t2 - t1)


if __name__ == '__main__':
    asyncio.run(main())
