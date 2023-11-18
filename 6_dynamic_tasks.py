import asyncio
import random
import time


async def foo(param):
    await asyncio.sleep(random.randint(1, 3))
    print(f'start foo with param {param}')
    await asyncio.sleep(random.randint(1, 3))
    print(f'end foo with param {param}')
    return 10 * param


async def main1():
    t1 = time.time()

    tasks = []
    for i in range(1, 6):
        tasks.append(asyncio.create_task(foo(i)))

    await asyncio.wait(tasks)

    print('-------------------------------------------')
    for task in tasks:
        print(task.result())
    print('-------------------------------------------')

    t2 = time.time()
    print(t2 - t1)


async def main2():
    t1 = time.time()
    tasks = []
    for i in range(1, 6):
        tasks.append(asyncio.create_task(foo(i)))

    results = await asyncio.gather(*tasks)

    print('-------------------------------------------')
    for result in results:
        print(result)
    print('-------------------------------------------')

    t2 = time.time()
    print(t2 - t1)


if __name__ == '__main__':
    asyncio.run(main2())
