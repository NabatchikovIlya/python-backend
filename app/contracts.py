from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    """
    Args:
        BaseModel (_type_): _description_
    """

    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
