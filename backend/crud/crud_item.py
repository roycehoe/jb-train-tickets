from typing import Callable

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models import Item as ItemModel
from schemas.item import ItemIn, ItemOut


class CRUDItem(CRUDBase[ItemModel, ItemIn, ItemOut]):
    def _get_order_by(self, sort_col: str, sort_order: str) -> Callable:
        sort_attr = getattr(self.model, sort_col)
        if sort_order == "asc":
            return sort_attr.asc()
        return sort_attr.desc()

    def search(
        self,
        db: Session,
        *,
        search_col: str = "",
        q: str = "",
        limit: int = 100,
        offset: int = 0,
        sort_col: str = "",
        sort_order: str = "asc",
    ) -> list[ItemModel]:
        order_by = self._get_order_by(sort_col, sort_order)
        return (
            db.query(self.model)
            .filter(getattr(self.model, search_col).like(f"{q}"))
            .order_by(order_by)
            .limit(limit)
            .offset(offset)
            .all()
        )


crud_item = CRUDItem(ItemModel)
