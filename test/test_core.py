
import pytest
from ..velox_telegram_bot.main import add
from ..blockchain.wallet import create_wallet

def test_create_wallet():
    wallet_address,private_key=create_wallet()
    print(f"wallet_address:{wallet_address}")
    assert len(str(wallet_address))==44
    assert len(private_key)==128

