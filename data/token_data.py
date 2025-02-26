from pydantic import  BaseModel
from typing import List
class BaseToken(BaseModel):
    address:str
    name: str
    symbol: str
class Pair(BaseModel):
    chainId:str
    dexId:str
    url:str
    pairAddress:str
    baseToken:BaseToken
class TokenData(BaseModel):
    schemaVersion:str
    pairs:List[Pair]





