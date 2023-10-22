from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class PublicPhotoSizes(BaseModel):
    medium: str
    mega_width: int
    mega: str
    small_width: int
    medium_width: int
    mega_height: int
    small_height: int
    large: str
    raw: str
    medium_height: int
    small: str
    large_width: int
    large_height: int


class Time(BaseModel):
    sort_order: int
    time: str
    time_iso: str
    utc_datetime: Optional[str] = None
    real_datetime_of_slot: Optional[str] = None
    duration: Optional[int] = None
    confirmation_include_end_time: Optional[bool] = None
    type: str
    access_rule_id: Optional[str] = None
    access_persistent_id: Optional[str]
    shift_persistent_id: Optional[str] = None
    is_held: Optional[bool] = None
    is_exclusive: Optional[bool] = None
    access_seating_area_id: Optional[Any] = None
    cc_party_size_min: Optional[Any] = None
    public_time_slot_description: Optional[str] = None
    public_description_title: str = "NA"
    public_photo: Optional[str] = None
    public_photo_sizes: Optional[PublicPhotoSizes] = None
    public_long_form_description: Optional[str] = None
    policy: Optional[str] = None
    cancellation_policy: Optional[str] = None
    custom_checkout_policy: Optional[str] = None
    pacing_limit: Optional[int] = None
    pacing_covers_remaining: Optional[int] = None
    upsell_categories: Optional[List] = None
    is_using_shift_upsells: Optional[bool] = None
    reservation_tags: Optional[List[str]] = None
    selected_automatic_upsells: Optional[List] = None
    experience_id: Optional[Any] = None
    default_service_charge: Optional[int] = None
    default_gratuity: Optional[int] = None
    service_charge_type: Optional[Any] = None
    require_credit_card: Optional[bool] = None
    cc_payment_rule: Optional[Any] = None
    charge_type: Optional[Any] = None
    cost: Optional[Any] = None
    apply_service_charge: Optional[bool] = None
    service_charge: Optional[Any] = None
    gratuity_type: Optional[Any] = None
    gratuity: Optional[Any] = None
    require_gratuity_charge: Optional[bool] = None
    tax_rate: Optional[Any] = None
    apply_gratuity_charge: Optional[bool] = None
    is_requestable: Optional[bool] = None


class AtlasAvailabilityResponse(BaseModel):
    name: str
    shift_persistent_id: str
    shift_id: str
    shift_category: str
    is_closed: bool
    upsell_categories: List
    times: List[Time]
    is_blackout: bool


class Data(BaseModel):
    availability: dict[str, list[dict]]


class AtlasResponse(BaseModel):
    status: int
    data: Data
    csrftoken: Any
