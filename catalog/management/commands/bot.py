import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram import Router, F
from django.conf import settings
from django.core.management.base import BaseCommand


bot = Bot(token=settings.TELEGRAM_API_KEY)
router = Router()
dp = Dispatcher()

button_categories = KeyboardButton(text="Show Categories")
keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_categories],],
    resize_keyboard=True,
    one_time_keyboard=False
)


@router.message(F.text == '/hello')
async def command_start(message: types.Message):
    await message.answer('Hello!', reply_markup=keyboard)


async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


class Command(BaseCommand):
    help = 'TG Bot for shop'

    def handle(self, *args, **kwargs):
        asyncio.run(main())
