from aiogram import Bot, dispatcher, types
import asyncio
from aiogram.filters import CommandStart

TOKEN = "8669455138:AAEs-vBP9IQoULVbIIqbUz8EwYfN5j6jZkE"

bot = Bot(token=TOKEN)

async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

    asyncio.run(main())
    @dp.message()
    async def echo (message: types.Message):
        await message.answer("Бот в разработке")
        @dp.message(CommandStart())
        async def start_end(message: type.Message):
            await message.answer("Привет! Это бот по продаже игровых товаров")