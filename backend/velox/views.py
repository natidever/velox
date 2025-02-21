import json
import logging
import  os
from dotenv import load_dotenv
from venv import logger

from aiogram import  types,Dispatcher,Bot
from django.http import HttpResponse,HttpRequest
from django.views.decorators.csrf import csrf_exempt
logging.basicConfig(level=logging.DEBUG)
load_dotenv()
telegram_token = os.environ.get('VELOX_TELEGRAM_TOKEN')
dp= Dispatcher()
bot=Bot(token=telegram_token)

def index(request):
    return HttpResponse("Velox Is The Fastest  Trading Bot On Solana")















# This going to be used when the system start using webhook
@csrf_exempt
async def handle_webhook(request:HttpRequest)->HttpResponse:
    recived_update=json.loads(request.body.decode('utf-8'))
    aiogram_formated_update=types.Update(**recived_update)
    logger.debug(f'aiogram_formated_update:{aiogram_formated_update}')
    await dp.feed_update(bot=bot,update=aiogram_formated_update)




