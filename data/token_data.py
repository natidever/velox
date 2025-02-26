from pydantic import  BaseModel
class TokenData(BaseModel):
    name:str
    price_native:float
    price_usd :float
    market_cap:float