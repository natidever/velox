import aiohttp
class SessionManager:
    def __init__(self):
        self.session=None
    async def get_session(self):
        self.session=aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10))
        return self.session
    async def close_session(self):
        if self.session:
            await self.session.close()

session_manager = SessionManager()
        
