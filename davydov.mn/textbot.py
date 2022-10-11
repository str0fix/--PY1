import asyncio
from datetime import datetime
class bot:
    def __init__(self):
        pass
    async def time_date(self):
        print ('[Server] Получаю дату и время')
        await asyncio.sleep(0.25)
        current_datetime = datetime.now()
        print('[Server] Получил! Думаю теперь что с этим делать!!')
        await asyncio.sleep(0.5)
        print(f'[Server] Дата: {current_datetime.day}.{current_datetime.month}.{current_datetime.year}\n'+
              f'[Server] Время: {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}')
    async def answer(self, text):
        await asyncio.sleep(0.5)
        print('[Server] Имитация мышления и обрабатывания букв...')
        await asyncio.sleep(0.5)
        if text=='Привет':
            print('[Server] Привет!')
        elif text==('привет'):
            print('[Server] Привет!!')
        elif (text==('Дата и время')) or (text=='Date time') or (text=='Дата') or (text=='Время'):
            task=asyncio.create_task(self.time_date())
            await task
        else:
            print('[Server] хм...')
            await asyncio.sleep(2)
            print('[Server] Моя твоя не понимает')