import  os
import  asyncio
import django
import sys
import random
from aiogram import  Bot,Dispatcher,types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from aiogram.utils.keyboard import  InlineKeyboardBuilder,InlineKeyboardButton

##Local Modules
from services.session_manager import session_manager
from services.price_service import PriceService

from blockchain.wallet import create_wallet
from callback_handler import transaction_router,bind_handler
from enums import Callback
from blockchain import database_functions

# Configuration
sys.path.append('/app/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()
load_dotenv()
telegram_token = os.environ.get('VELOX_TELEGRAM_TOKEN')
dp= Dispatcher()
bot=Bot(token=telegram_token)
#


@dp.message(CommandStart())
async def handle_start(msg:types.Message )->None:
    # public,private=create_wallet()
    # user_id=msg.from_user.id
    dev_user_id=int(random.random()*1000000)
    print(f'user_id:{dev_user_id}')
    # user ,wallet =await database_functions.store_user_and_wallet(
    #     user_id=dev_user_id,
    #     private_key=private,
    #     wallet_address=public
    # )
    print(f"User and Wallet are Created and Stored :Wallet")
    keyboard=InlineKeyboardBuilder()

    keyboard.row(
        InlineKeyboardButton(text="Buy", callback_data=Callback.BUY.value),
        InlineKeyboardButton(text="Sell", callback_data='sell_action')
    )
    await msg.answer(text=f"Your wallet address : " ,reply_markup=keyboard.as_markup())



dp.include_router(transaction_router)
bind_handler(dp)
async def main()->None:
   prs= PriceService()
   response=await prs.get_token_detail("TRUMP")
   from data.token_data import TokenData
   from pydantic import ValidationError, validate_call
   try:
      token_data =TokenData.model_validate(response)
      first_pair=token_data.pairs[0]
      address=first_pair.pairAddress

      print(f"formated_response :{address}")
   except ValidationError as exc:
      print(f"Error :{repr(exc.errors()[0]['type'])}")


   await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

