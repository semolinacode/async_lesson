import asyncio
import random


async def foo(param):
    await asyncio.sleep(random.randint(1, 3))
    print(f'start foo with param {param}')
    await asyncio.sleep(random.randint(1, 3))
    print(f'end foo with param {param}')


async def main():
    await foo(1)

if __name__ == '__main__':
    asyncio.run(main())
