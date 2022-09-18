from fastapi import APIRouter
from typing import Optional
from app.contracts import Item

router = APIRouter()


@router.get("/")
async def root():
    """base function for print hello world

    Returns:
        _type_: _description_
    """

    return {"message": "Hello World"}


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    """base function for print hello world with item_id

    Returns:
        _type_: _description_
    """

    return {"item_id": item_id}


@router.get("/users/")
async def read_user(user_id: int, query: Optional[str] = None):
    """base query function

    Returns:
        _type_: _description_
    """
    if query:
        return {"user_id": user_id, "query": query}
    return {"user_id": user_id}


@router.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, query: Optional[str] = None, short: bool = False
):
    """base query function with items and users

    Returns:
        _type_: _description_
    """
    item = {"item_id": item_id, "owner_id": user_id}
    if query:
        item.update({"query": query})
    if not short:
        item.update({"description": "Additionaly var"})
    return item


@router.post("/items/")
async def create_item(item: Optional[Item] = None):
    """base query function

    Returns:
        _type_: _description_
    """
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
