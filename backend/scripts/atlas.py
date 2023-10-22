from dataclasses import dataclass
from datetime import date, datetime

import httpx
from schemas.atlas import AtlasAvailabilityResponse, AtlasResponse, Time

ATLAS_AVAILABILITY_BASE_URL = "https://www.sevenrooms.com/api-yoa/availability/widget/range?venue=atlassg&time_slot=18:00&party_size=2&halo_size_interval=50&num_days=1"


@dataclass
class AtlasAvailability:
    date: date
    time: str
    is_available: bool
    dining_type: str


async def get_atlas_response(date: date) -> AtlasResponse:
    try:
        url = f'{ATLAS_AVAILABILITY_BASE_URL}&start_date={date.strftime("%m-%d-%Y")}'

        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  # Raise an exception for non-2xx status codes

            return AtlasResponse(**response.json())
    except Exception as e:
        print("Something went wrong:", e)
        raise Exception("Failed to fetch Atlas response")


async def get_atlas_availability_response(date: date) -> AtlasAvailabilityResponse:
    atlas_availability_response = await get_atlas_response(date)
    return [
        AtlasAvailabilityResponse(**availability)
        for availability in atlas_availability_response.data.availability[
            date.strftime("%Y-%m-%d")
        ]
    ][0]


def parse_atlas_availability(date: date, time: Time) -> AtlasAvailability:
    return AtlasAvailability(
        date=date,
        time=time.time,
        is_available=time.public_description_title != "NA",
        dining_type=time.public_description_title,
    )


async def get_atlas_availability(date: str) -> list[AtlasAvailability]:
    formatted_date = datetime.strptime(date, "%d-%m-%Y")
    atlas_availabilty_response = await get_atlas_availability_response(formatted_date)
    return [
        parse_atlas_availability(formatted_date, i)
        for i in atlas_availabilty_response.times
    ]
