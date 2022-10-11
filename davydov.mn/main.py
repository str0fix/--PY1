import textbot as bot

async def tic():
    while True:
        await bot.asyncio.sleep(1.5)

async def main():
    bot.asyncio.create_task(tic())
    var = bot.bot()
    while True:
        query = await bot.asyncio.to_thread(input)
        await var.answer(query)
try:
    bot.asyncio.run(main())
except KeyboardInterrupt:
    print('\n[Server] Завершение программы...\n')