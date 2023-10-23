from typing import Any, Literal

from fastapi import APIRouter, Depends, HTTPException, status
from loguru import logger
from scripts.tickets import get_train_tickets_availability
from sqlalchemy.orm import Session

router = APIRouter(tags=["Tickets"])


@router.get("/{direction}/{date}", status_code=status.HTTP_200_OK, response_model=Any)
def search(date: str, direction: str):
    return get_train_tickets_availability(date, direction)
