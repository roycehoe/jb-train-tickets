<script setup lang="ts">
import { Err, Ok, Result } from "ts-results";
import { Ref, onBeforeMount, ref, watch } from "vue";
import { client } from "../../services";

export interface TicketAvailabilityData {
  departure_time: string;
  arrival_time: string;
  duration: string;
  seat_count: string;
  price: string;
}

const props = defineProps<{
  date: Date;
  timeslots: string[];
}>();
const isLoading: Ref<boolean> = ref(false);
const availabilities: Ref<TicketAvailabilityData[]> = ref([]);
const day: Ref<Date> = ref(props.date);
const timeslots: Ref<string[]> = ref(props.timeslots);
const noDataFromApi: Ref<boolean> = ref(false);

async function getTicketAvailabilityResponse(
  date: string
): Promise<Result<TicketAvailabilityData[], any>> {
  try {
    const response = await client.get(date);
    return Ok(response.data as TicketAvailabilityData[]);
  } catch (error) {
    return Err(error);
  }
}

function getApiFormattedDate(date: Date): string {
  const day = ("0" + date.getDate()).slice(-2);
  const month = ("0" + date.getMonth()).slice(-2);
  const year = date.getFullYear();

  return `${year}-${month}-${day}`;
}

function isAvailableForDrinks(timeslot: string) {
  const timeslotData = availabilities.value.filter((availability) => {
    return (
      availability.departure_time === timeslot &&
      availability.seat_count !== "0"
    );
  });
  return timeslotData.length !== 0;
}

function getTooltip(timeslot: string) {
  const timeslotData = availabilities.value.filter((availability) => {
    return availability.departure_time === timeslot;
  });
  return timeslotData[0].seat_count;
}

async function loadPage() {
  isLoading.value = true;
  const apiFormattedDate = getApiFormattedDate(day.value);
  const response = await getTicketAvailabilityResponse(apiFormattedDate);
  if (response.ok) {
    availabilities.value = response.val;
  } else {
    noDataFromApi.value = true;
  }
  console.log(availabilities.value);
  isLoading.value = false;
}

onBeforeMount(async () => {
  await loadPage();
});

watch(props, async (newProps) => {
  day.value = newProps.date;
  noDataFromApi.value = false;
  await loadPage();
});
</script>

<template>
  <ul v-if="!noDataFromApi">
    <li v-for="timeslot in timeslots">
      <span v-if="isLoading" class="loading loading-spinner w-4 h-4"></span>
      <div
        v-else-if="isAvailableForDrinks(timeslot)"
        class="tooltip w-4 h-4 bg-success rounded-sm"
        :data-tip="getTooltip(timeslot)"
      ></div>

      <div
        v-else
        class="tooltip w-4 h-4 bg-neutral rounded-sm"
        :data-tip="timeslot"
      ></div>
    </li>
  </ul>
</template>

<style scoped></style>
