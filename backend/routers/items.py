from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, status
from loguru import logger
from sqlalchemy.orm import Session

import models
from constants import PREPOPULATED_ITEMS
from crud.crud_item import crud_item
from database import get_db
from schemas.item import ItemIn, ItemOut
from services.items import create_many_items, get_all_items, search_items

SortOrder = Literal["asc", "desc"]
router = APIRouter(tags=["Items"], prefix="/items")


@router.on_event("startup")
def prepopulate_db(prepopulated_items: list[dict] = PREPOPULATED_ITEMS):
    logger.info("prepopulating database with mock data")
    db = next(get_db())
    items = [models.Item(**data) for data in prepopulated_items]
    for item in items:
        crud_item.create(db, obj_in=item)
    db.close()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_many(new_items: list[ItemIn], db: Session = Depends(get_db)):
    try:
        create_many_items(new_items, db)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Unable to create many")


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[ItemOut])
def get_all(db: Session = Depends(get_db)):
    try:
        return get_all_items(db)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Unable to get all items")


@router.get("/search", status_code=status.HTTP_200_OK, response_model=list[ItemOut])
def search(
    search_col: str,
    q: str,
    limit: int = 100,
    offset: int = 0,
    sort_col: str = "",
    sort_order: SortOrder = "asc",
    db: Session = Depends(get_db),
):
    try:
        return search_items(
            db=db,
            search_col=search_col,
            q=q,
            limit=limit,
            offset=offset,
            sort_col=sort_col,
            sort_order=sort_order,
        )
    except Exception:
        raise HTTPException(status_code=404, detail=f"Unable to search items")
