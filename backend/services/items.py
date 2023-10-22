from typing import Literal

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.crud_item import crud_item
from database import get_db
from schemas.item import ItemIn

SortOrder = Literal["asc", "desc"]


def create_many_items(new_items: list[ItemIn], db: Session = Depends(get_db)):
    try:
        return [crud_item.create(db, obj_in=item) for item in new_items]
    except Exception:
        raise Exception


def get_all_items(db: Session = Depends(get_db)):
    try:
        return crud_item.get_multi(db)
    except Exception:
        raise Exception


def search_items(
    db: Session,
    search_col: str,
    q: str,
    limit: int = 100,
    offset: int = 0,
    sort_col: str = "",
    sort_order: SortOrder = "asc",
):
    try:
        return crud_item.search(
            db,
            search_col=search_col,
            q=q,
            limit=limit,
            offset=offset,
            sort_col=sort_col,
            sort_order=sort_order,
        )
    except Exception:
        raise Exception
