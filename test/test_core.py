import os
import sys

ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # Moves up two levels
PARENT_DIR = os.path.dirname(ROOT_DIR)
sys.path.append(PARENT_DIR)

from bot.blockchain.wallet import create_wallet


def test_create_wallet():
    wallet_address,private_key=create_wallet()
    print(f"wallet_address:{wallet_address}")
    assert len(str(wallet_address))==44
    assert len(private_key)==128

