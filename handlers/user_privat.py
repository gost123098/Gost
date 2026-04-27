from aiogram.filters import CommandStart, Command
from aiogram import types, Router

user_router = Router()

@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет\nЭто бот для продажи, чтобы узнать информацию о командах бота напишите '/info'")

@user_router.message(Command("shop"))
async def shop(message: types.Message):
    await message.answer("Валюта: 2 кристалла - 1 звезда")


@user_router.message(Command("info"))
async def info(message: types.Message):
    await message.answer("Команды:")

@user_router.message(Command("daily"))
async def daily(message: types.Message):
    await message.answer("Награды, которые даются каждый день:")

@user_router.message()
async def echo(message: types.Message):
    await message.answer("Бот пока в разработке")