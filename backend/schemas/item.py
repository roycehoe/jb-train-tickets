from pydantic import BaseModel


class ItemIn(BaseModel):
    """The request body when new items are created"""

    name: str
    quantity: int
    price: float
    description: str


class ItemOut(BaseModel):
    """The response body when items database is queried"""

    id: int
    name: str
    quantity: int
    price: float
    description: str

    class Config:
        orm_mode = True
