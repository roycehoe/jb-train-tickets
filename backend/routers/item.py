from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from schemas.item import ItemIn, ItemOut
from services.item import create_item, delete_item, get_item, update_item

router = APIRouter(tags=["Item"], prefix="/item")


@router.get("/{item_id}", status_code=status.HTTP_200_OK, response_model=ItemOut)
def get(
    item_id: int,
    db: Session = Depends(get_db),
):
    try:
        return get_item(item_id, db)
    except Exception:
        raise HTTPException(
            status_code=404, detail=f"Item with item_id: {item_id} not found"
        )


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: ItemIn, db: Session = Depends(get_db)):
    try:
        return create_item(request, db)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Failed to create item: {request}",
        )


@router.put("/{item_id}", status_code=status.HTTP_201_CREATED)
def update(item_id: int, updated_item: ItemIn, db: Session = Depends(get_db)):
    try:
        return update_item(item_id, updated_item, db)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item of item_id {item_id} not found",
        )


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, db: Session = Depends(get_db)):
    try:
        return delete_item(item_id, db)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item of item_id {item_id} not found",
        )
