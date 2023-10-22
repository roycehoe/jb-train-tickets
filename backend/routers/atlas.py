from typing import Any, Literal

from fastapi import APIRouter, Depends, HTTPException, status
from loguru import logger
from scripts.atlas import get_atlas_availability
from sqlalchemy.orm import Session

router = APIRouter(tags=["Atlas"])


@router.get("/{date}", status_code=status.HTTP_200_OK, response_model=Any)
async def search(date):
    return await get_atlas_availability(date)
