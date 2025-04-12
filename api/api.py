from fastapi import APIRouter, Depends
from .db import get_db

router = APIRouter()

@router.get("/items/")
async def read_items(db=Depends(get_db)):
    return {"items": "This is a placeholder"}
