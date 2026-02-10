from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    quantity: int
    price: float
    description: Optional[str] = None # string o None

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    description: Optional[str] = None
