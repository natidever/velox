from aiogram import types, Router
from aiogram.fsm.context import  FSMContext
from fsm_forms import BuyState
from aiogram import F
# Local Modules
from enums import Callback
##Variables
transaction_router=Router()

async def buy_callback(callback:types.CallbackQuery,state:FSMContext):
    await callback.message.answer(text="What Token You want to buy")
    await state.set_state(BuyState.accept_token)
    await callback.answer()



@transaction_router.message(BuyState.accept_token)
async def accept_token(msg:types.Message,state:FSMContext):
    await state.update_data(token=msg.text)
    data = await state.get_data()
    token=data.get("token","Unknown Token")
    resutl=get_token_detail(token)
    # if token not found
    #send try again
    #if result
    #retun the result

    print(f"Token :{token}")
    await msg.answer(text=f"Token:{token}")



def bind_handler(dp):
    dp.callback_query.register(buy_callback, F.data == Callback.BUY.value)

 # def get_token_detail(token:str):
 #     pass


#      if result.statuscode == 200:
#             return result.data
#     else:
#       TOKEN_NOT_FOUND=TRUE



#



