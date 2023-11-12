import { client } from "@/services";
import { Err, Ok, Result } from "ts-results";
import { Ref, ref } from "vue";

export interface TicketAvailabilityData {
  departure_time: string;
  arrival_time: string;
  duration: string;
  seat_count: string;
  price: string;
}

export function useTicketAvailability() {
  const ticketAvailability: Ref<TicketAvailabilityData[]> = ref([]);

  function _formatWithLeadingZero(number: number): string {
    const numberStr = number.toString();
    if (number < 10) {
      return "0" + numberStr;
    }
    return numberStr;
  }

  function _getApiFormattedDate(date: Date): string {
    const day = _formatWithLeadingZero(date.getDate());
    const month = _formatWithLeadingZero(date.getMonth() + 1);
    const year = date.getFullYear();

    return `${year}-${month}-${day}`;
  }

  async function _getTicketAvailabilityResponse(
    date: Date,
    currentTravelDirection: string
  ): Promise<Result<TicketAvailabilityData[], any>> {
    try {
      const formattedDate = _getApiFormattedDate(date);
      const response = await client.get(
        `${currentTravelDirection}/${formattedDate}`
      );
      return Ok(response.data as TicketAvailabilityData[]);
    } catch (error) {
      return Err(error);
    }
  }

  async function createTicketAvailabilityResponse(
    date: Date,
    currentTravelDirection: string
  ) {
    const ticketAvailabilityResponse = await _getTicketAvailabilityResponse(
      date,
      currentTravelDirection
    );
    if (ticketAvailabilityResponse.ok) {
      ticketAvailability.value = ticketAvailabilityResponse.val;
      return;
    }
  }

  function getTooltipText(timeslot: string) {
    if (ticketAvailability.value.length === 0) {
      return "";
    }
    const timeslotData = ticketAvailability.value.filter((availability) => {
      return availability.departure_time === timeslot;
    });
    if (!timeslotData[0]) {
      return "";
    }
    return `${timeslotData[0].seat_count} seats at ${timeslot}`;
  }

  function isAvailableForBooking(timeslot: string) {
    if (ticketAvailability.value.length === 0) {
      return false;
    }
    const timeslotData = ticketAvailability.value.filter((availability) => {
      return (
        availability.departure_time === timeslot &&
        availability.seat_count !== "0"
      );
    });
    return timeslotData.length !== 0;
  }

  return {
    ticketAvailability,
    createTicketAvailabilityResponse,
    getTooltipText,
    isAvailableForBooking,
  };
}
