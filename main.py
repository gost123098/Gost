from aiogram import Bot, Dispatcher
import asyncio

TOKEN = "8669455138:AAEs-vBP9IQoULVbIIqbUz8EwYfN5j6jZkE"

bot = Bot(token=TOKEN)
dp = Dispatcher()


from handlers.user_privat import user_router
dp.include_router(user_router)


async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

asyncio.run(main())