import asyncio

import aiohttp
from constants.endpoints import DEX_SCREENER
from data.token_data import TokenData
from services.session_manager import session_manager
class PriceService:
    def __init__(self):
        self.base_url=DEX_SCREENER
    async def get_token_detail(self,symbol):
        session= await session_manager.get_session()
        try:
            response=await session.get(f"{self.base_url}/latest/dex/search/?q={symbol}&network=solana")
            if response.status == 200 :
                return await response.json()
            return None
        except (aiohttp.ClientError,asyncio.TimeoutError) as e :
            print(f"Error During Fetching price of the token {e}")



