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

    tasks = [
        asyncio.create_task(foo(1)),
        asyncio.create_task(foo(2)),
        asyncio.create_task(foo(3)),
    ]

    done, pending = await asyncio.wait(tasks)

    # print('-------------------------------------------')
    # print('Done:')
    # for d in done:
    #     print(d, '|', d.result())
    # print('Pending:')
    # for p in pending:
    #     print(p)
    # print('-------------------------------------------')

    print('*******************************************')
    for task in tasks:
        print(task.result())
    print('*******************************************')

    t2 = time.time()
    print(t2 - t1)


async def main2():
    t1 = time.time()
    results = await asyncio.gather(
        asyncio.create_task(foo(1)),
        asyncio.create_task(foo(2)),
        asyncio.create_task(foo(3)),
    )

    print('-------------------------------------------')
    print(results)
    for result in results:
        print(result)
    print('-------------------------------------------')

    t2 = time.time()
    print(t2 - t1)


if __name__ == '__main__':
    asyncio.run(main2())
