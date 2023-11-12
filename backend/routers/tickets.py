from typing import Any, Literal

from fastapi import APIRouter, Depends, HTTPException, status
from loguru import logger
from sqlalchemy.orm import Session

from exceptions import NoTripDataException
from scripts.tickets import TicketData, get_train_tickets_availability

router = APIRouter(tags=["Tickets"])


@router.get(
    "/{direction}/{date}",
    status_code=status.HTTP_200_OK,
    response_model=list[TicketData],
)
def search(date: str, direction: str):
    try:
        return get_train_tickets_availability(date, direction)
    except NoTripDataException:
        return []
