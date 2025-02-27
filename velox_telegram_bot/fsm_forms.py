from aiogram.filters.state import State,StatesGroup
class BuyState(StatesGroup):
    accept_token=State()
