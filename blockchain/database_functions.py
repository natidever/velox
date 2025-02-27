
import os
from asgiref.sync import async_to_sync, sync_to_async
import sys
sys.path.append('/app/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

import django

django.setup()
from velox.models import Users, Wallet


# from channels.db import database_sync_to_async




@sync_to_async
def store_user_and_wallet(user_id,wallet_address,private_key):
    """Function to store user and walle """
    print("Database function is running ")

    # user=Users.objects.create(
    #     user_id=user_id)
    user = Users.objects.create(
        user_id=user_id)

    wallet=Wallet.objects.create(
        user=user,
        wallet_address=wallet_address,
        private_key=private_key
    )
    return user,wallet

if __name__ == "__main__":
    store_user_and_wallet(user_id='',wallet_address='',private_key='')
