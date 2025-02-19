

from bot.constants.endpoints import DEV_NET_URL

from solders.keypair import Keypair
from solana.rpc.api import Client



def create_wallet():
    key_pair = Keypair()
    private_key = bytes(key_pair).hex()
    wallet_address= key_pair.pubkey()
    return wallet_address,private_key

def check_wallet_balance(public_key):
        client = Client(DEV_NET_URL)
        wallet_data=client.get_balance(pubkey=public_key)
        wallet_balance=wallet_data.value
        print(f"wallet_balance :- {wallet_balance}SOL")


public_address ,private_keys=create_wallet()
check_wallet_balance(public_address)













# print(f"wallet_address :{wallet_address}")
# print(f"private_key :{private_key}")
#
# ## Test if the wallet is correctly created by checking the account balance of SOL
#
# client = Client("https://api.devnet.solana.com")
# wallet_balance = client.get_balance(wallet_address)
# print(f"WALLET_BALANCE :{wallet_balance}")



