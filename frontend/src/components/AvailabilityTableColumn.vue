<script setup lang="ts">
import { useTicketAvailability } from "@/composables/useTicketAvailability";
import { Ref, onBeforeMount, ref, watch } from "vue";
export interface TicketAvailabilityData {
  departure_time: string;
  arrival_time: string;
  duration: string;
  seat_count: string;
  price: string;
}

const {
  ticketAvailability,
  createTicketAvailabilityResponse,
  getTooltipText,
  isAvailableForBooking,
} = useTicketAvailability();

const props = defineProps<{
  date: Date;
  timeslots: string[];
}>();
const isLoading: Ref<boolean> = ref(false);
const day: Ref<Date> = ref(props.date);
// const timeslots: Ref<string[]> = ref(props.timeslots);
const noDataFromApi: Ref<boolean> = ref(false);

async function loadPage() {
  isLoading.value = true;
  await createTicketAvailabilityResponse(day.value);
  isLoading.value = false;
}

onBeforeMount(async () => {
  console.log("hello");
  await loadPage();
});

onBeforeMount(() => {
  console.log("hello");
});

watch(props, async (newProps) => {
  day.value = newProps.date;
  noDataFromApi.value = false;
  await loadPage();
});
</script>

<template>
  <ul>
    <li v-for="timeslot in timeslots">
      <span v-if="isLoading" class="loading loading-spinner w-4 h-4"></span>
      <div v-else class="tooltip w-4 h-4 rounded-sm"></div>
      <div
        v-else
        class="tooltip w-4 h-4 rounded-sm"
        :class="isAvailableForBooking(timeslot) ? 'bg-success' : 'bg-neutral'"
        :data-tip="getTooltipText(timeslot)"
      ></div>
    </li>
  </ul>
</template>

<style scoped></style>
