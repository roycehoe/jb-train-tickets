from fastapi import Depends
from sqlalchemy.orm import Session

from crud.crud_item import crud_item
from database import get_db
from models import Item
from schemas.item import ItemIn


def get_item(
    item_id: int,
    db: Session,
) -> Item:
    try:
        if item := crud_item.get(db, item_id):
            return item
        raise Exception
    except Exception:
        raise Exception


def create_item(request: ItemIn, db: Session) -> Item:
    if created_item := crud_item.create(db, obj_in=request):
        return created_item
    raise Exception


def update_item(item_id: int, updated_item: ItemIn, db: Session) -> Item:
    try:
        db_obj = crud_item.get(db, item_id)
        return crud_item.update(db, db_obj=db_obj, obj_in=updated_item.dict())
    except Exception:
        raise Exception


def delete_item(item_id: int, db: Session = Depends(get_db)) -> Item:
    try:
        return crud_item.delete(db, id=item_id)
    except Exception:
        raise Exception
