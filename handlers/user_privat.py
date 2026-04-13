
from aiogram.filters import CommandStart, Command
from aiogram import types, Router

user_router = Router()

@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет\nЭто бот для продажи")

@user_router.message(Command("catalog"))
async def catalog(message: types.Message):
    await message.answer("Привет, это каталог!")

@user_router.message(Command("Lisa"))
async def Lisa(message: types.Message):
    await message.answer("Привет, булка! Я тебя люблю!!!")

@user_router.message()
async def echo(message: types.Message):
    await message.answer("Бот пока в разработке")