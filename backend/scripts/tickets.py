from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, List, Optional

import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel, ValidationError

from exceptions import NoTripDataException


class TrainDirection(Enum):
    JB_TO_SG = auto()
    SG_TO_JB = auto()


class GetTicketDataResponse(BaseModel):
    status: bool
    messages: List
    messageCode: Any
    data: str


@dataclass
class TicketData:
    departure_time: str
    arrival_time: str
    duration: str
    seat_count: str
    price: str


BASE_URL = "https://shuttleonline.ktmb.com.my/ShuttleTrip/Trip"
JB_TO_SG_DEFAULT_PARAMS = {
    "SearchData": "2l8QL3futET6vQA3B8o6GzzrslIM/2zkXeyhUBg8/SE291QxID/uke1d3ZFaL46WCg3e79YQuh36Lmo6sOIjGxkPz3wIJ1qx9pxio2fN0px6yKBEyDBI/ybF5udtbeoA6pUZgS0RMbMPm1CVaNNwaKnndpWHZQ7z2vYQOxTYar0CVs2ar9ZZ2vYa51r47nUxvEGNpzjTTqJBsiCat3RuVBh+ecjpKl1Y94kq7jLUIIId3pTPRd9KzsJtM5Pd+wmxEmA6QnPAyR57WCYZsfs24ab16YQNe9AMK01Ilt8eb4rwt31F/SJyMN17jCuof5D0YPBomBaX3SJ7G5SGwaf5MA7q+LTdXm9vcbEi0iFmlsYOBunTDa/ICkYRuObPsntbgjRcPIeghCzQjUj2DC6/E4MapE4KXHN7J2qkGvsHEJd4nRNZN8qMZgMEeCLEc0Wlq4PRVMYYVsOeZHx00Q4OeJUUD3MoxVH1tH5oqdIWVbX0HcPdH9My43vBbN4P9AKYCepGNQwu3SMzrNzgRQelwQ==",
    "FormValidationCode": "C5IHRlP7C7qajUAZ+30DAadJinpblozJVWaLFIws8NINmWdz1UqkPiGOeOcBJnhm8qcQiTMyVadZsPj/ZTEZl9NHCJlbFEetfDnE2cNp1OB6ahDMHXeqZDRuwkijBBpy9Ya604Ye9NicObSWpqgQWg==",
    "IsReturn": False,
    "BookingTripSequenceNo": 1,
}
SG_TO_JB_DEFAULT_PARAMS = {
    "SearchData": "6SN8zIJwfhnVRS+xG2fLUP0zpes3f5P2G2vjS3HnuZ9WIy/20rv7g6Is53et5szYXXxNV+avwvZd16cUNmPbtSz91DwWM6Tzeyn5Ay62aSLzr1J+7BFRDAfMI0lb27nEJ7coNAdvVFy97ap1R1qFgs5o4lfj2jyLQKeZBzKpxSTP+PVIFpilBkdlOyuo5Yi8nnCpkyS4F9A1x/IABcI6ESD3971F0IiVhHk5wpt5NgtWBLXlDFtKjU2DSIGi1D7LlQSMfahSv0auSS1HqLG7V8qiGGurhcjVQj83j/VajpM9JJG1w1teaAGNabfp/VZBR0ZTKqbKqX5eaui76/bwJK3M8oLjrY/Zj1lg4xKvlDX1O41+vInYVgmW9jKDB9Au1AJfaWVJ/ZeW2oe1I25RDn5OndgoMpGdYkl1Y0aCMfKepKgMbFSlnCsBTZq1GKRN2KsaHuf6s7bPRWGbYuB7Fy0TyqiuzM+GcHaV53h85flTTxJHreE6OQ2ohE0RyoqDmrAinNvQI8Qwakb57nh+5g==",
    "FormValidationCode": "NoxYG0VASPKHvZh1sHwJ5DqHEhjErMFctJmmuVjGPaKgJrQlzKYYHQJVA3sM2ECwcsoRilDpUiet8vk3O4zN72FDNnkYfyNx1d9ZUa8jM/UIA/2WHCody7xDajlL+gBp3R3SsZTXHoWQ4RLs2V8Mkw==",
    "IsReturn": False,
    "BookingTripSequenceNo": 1,
}
DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "RequestVerificationToken": "CfDJ8INTwVi1HQZGsxUoHywWuIP8C5y9FGqoTq0r9nzr-sk00uD62bghl-b_3nb9p79wxH2Xo0C2pJ1QyAWKC9WWUsSTrX25nM7k8IiGhxZWfQt9ZgdqFMFF5LINsq1Ek_EBHDcq1QL8DY69kNUNZ6IUUOQ",
    "Cookie": "_ga_51BS0V6RLH=GS1.1.1697960907.4.1.1697961685.0.0.0; _ga=GA1.3.1521485548.1697773729; _gcl_au=1.1.1409948139.1697773732; X-CSRF-TOKEN-COOKIENAME=CfDJ8INTwVi1HQZGsxUoHywWuIMNQwp0xxVj4IxVhijKWR9im01YeNk7ijKqpOrMsPEs6zXab5egNbP6eqJAkX5O8hj21fRkC3RE2SLpt_HEK2OJjSr430Ut_NqtMlDq_oaDLyHpTz-BQtaxzuJO9DHpTDM; _ga_FMJBCXCPGC=GS1.1.1697786817.1.1.1697786828.49.0.0; _gid=GA1.3.28437549.1697960908; _gat_gtag_UA_175560898_1=1",
}


def get_jb_to_sg_train_tickets_response(date: str) -> GetTicketDataResponse:
    try:
        response = requests.post(
            url=BASE_URL,
            json={**JB_TO_SG_DEFAULT_PARAMS, "DepartDate": date},
            headers=DEFAULT_HEADERS,
        )
        return GetTicketDataResponse(**response.json())

    except ValidationError:
        raise NoTripDataException


def get_sg_to_jb_train_tickets_response(date: str) -> GetTicketDataResponse:
    try:
        response = requests.post(
            url=BASE_URL,
            json={**SG_TO_JB_DEFAULT_PARAMS, "DeparteDate": date},
            headers=DEFAULT_HEADERS,
        )
        return GetTicketDataResponse(**response.json())

    except ValidationError:
        raise NoTripDataException


def get_ticket_data(ticket_html: str) -> list[TicketData]:
    soup = BeautifulSoup(ticket_html, "html.parser")

    # Extract table rows
    rows = soup.select("tbody.depart-trips tr")

    # Extract data into dictionary
    table_data: list[TicketData] = []
    for row in rows:
        train_service = [i.text.strip() for i in row.find_all("td")]
        _, departure_time, arrival_time, duration, seat_count, price, _ = train_service
        table_data.append(
            TicketData(
                departure_time=departure_time,
                arrival_time=arrival_time,
                duration=duration,
                seat_count=seat_count,
                price=price,
            )
        )
    return table_data


def get_train_direction(direction: str) -> TrainDirection:
    if direction == "sg-to-jb":
        return TrainDirection.SG_TO_JB
    return TrainDirection.JB_TO_SG


def get_train_tickets_response(date: str, direction: str):
    train_direction = get_train_direction(direction)
    try:
        if train_direction == TrainDirection.JB_TO_SG:
            return get_jb_to_sg_train_tickets_response(date)
        return get_sg_to_jb_train_tickets_response(date)
    except NoTripDataException:
        raise NoTripDataException


def get_train_tickets_availability(date: str, direction: str) -> list[TicketData]:
    try:
        train_tickets_response = get_train_tickets_response(date, direction)
        return get_ticket_data(train_tickets_response.data)
    except NoTripDataException:
        raise NoTripDataException
