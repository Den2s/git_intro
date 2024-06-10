import asyncio


async def hello():
    print('Запуск функции hello')
    await asyncio.sleep(5)  # Отдаем управление обратно в Event loop пока ждём
    print('Переключение контекста в функцию hello')
    return 'Выполнена функция hello'


async def bye():
    print('Запуск функции bye')
    await asyncio.sleep(2)  # Отдаем управление обратно в Event loop пока ждём
    print('Переключение контекста в функцию byе')
    return 'Выполнена функция bye'


async def starter(ioloop):
    tasks = [ioloop.create_task(hello()), ioloop.create_task(bye())]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    result = done.pop().result()

    for pending_future in pending:
        pending_future.cancel()

    print(result)


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(starter(ioloop))
ioloop.close()
