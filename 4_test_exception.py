import asyncio
import random
import time


'''
asyncio.gather() принимает список асинхронных задач (coroutines) в качестве аргументов и запускает их одновременно.
Она возвращает список результатов, соответствующих выполненным задачам в том же порядке, в котором задачи были переданы в функцию.
Если во время выполнения задачи возникает исключение, asyncio.gather() 
прекращает выполнение остальных задач и сразу же выбрасывает исключение.

asyncio.wait() принимает список асинхронных задач (coroutines) в качестве аргументов и запускает их одновременно.
Она возвращает кортеж из двух множеств: множество выполненных задач и множество невыполненных задач.
Если во время выполнения задачи возникает исключение, asyncio.wait() 
ПРОДОЛЖАЕТ выполнение остальных задач и не выбрасывает исключение.
'''


async def foo(param):
    await asyncio.sleep(random.randint(1, 3))

    if param == 2:
        raise ValueError('Моё собственное исключение')

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


async def main3():
    t1 = time.time()

    tasks = [
        asyncio.create_task(foo(1)),
        asyncio.create_task(foo(2)),
        asyncio.create_task(foo(3)),
    ]

    '''
    Когда вы передаете список асинхронных задач в asyncio.as_completed(), 
    она возвращает итератор, итерирование по которому возвращает завершившиеся задачи. 
    Это позволяет вам обрабатывать задачи, как только они завершаются, в том порядке, 
    в котором они завершились, вместо того чтобы ждать завершения всех задач сразу.
    '''

    for completed_task in asyncio.as_completed(tasks):
        try:
            await completed_task
        except ValueError:
            print(f'Caught ValueError in task: {completed_task}')
    t2 = time.time()
    print(t2 - t1)


if __name__ == '__main__':
    asyncio.run(main3())
