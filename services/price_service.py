import asyncio

import aiohttp
from constants.enpoints import DEX_SCREENER
from data.token_data import TokenData
from session_manager import session_manager
class PriceService:
    def __init__(self):
        self.base_url=DEX_SCREENER
    async def get_token_detail(self,symbol):
        session= session_manager.get_session()
        try:
            response=session.get(f"{self.base_url}/latest/dex/search/?q={symbol}&network=solana")
            if response.status == 200 :
                return response.json()
            return None
        except (aiohttp.ClientError,asyncio.TimeoutError) as e :
            print(f"Error During Fetching price of the token {e}")



