from aiogram import  Bot,Dispatcher,types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
import  os
import  asyncio
##Local Modules
from bot.blockchain.wallet import create_wallet
load_dotenv()
telegram_token = os.environ.get('VELOX_TELEGRAM_TOKEN')
dp= Dispatcher()
bot=Bot(token=telegram_token)

@dp.message(CommandStart)
async def handle_start(msg:types.message)->None:
    public,private=create_wallet()
    await msg.answer(text=f"Wallet Address:{public}")



async def main()->None:
   await bot.delete_webhook()
   await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())