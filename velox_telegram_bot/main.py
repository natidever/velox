from aiogram import  Bot,Dispatcher,types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
import  os
import  asyncio
load_dotenv()
telegram_token = os.environ.get('VELOX_TELEGRAM_TOKEN')
dp= Dispatcher()
bot=Bot(token=telegram_token)

@dp.message(CommandStart)
async def handle_start(msg:types.message)->None:
    await msg.answer(text="STARTED")


async def main()->None:
   await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())



