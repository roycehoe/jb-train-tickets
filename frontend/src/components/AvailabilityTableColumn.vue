<script setup lang="ts">
import { useTicketAvailability } from "@/composables/useTicketAvailability";
import { currentTravelDirection } from "@/composables/useTravelDirection";
import { Ref, onBeforeMount, ref, watchEffect } from "vue";

const {
  getOpacity,
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

async function loadColumn() {
  isLoading.value = true;
  await createTicketAvailabilityResponse(
    props.date,
    currentTravelDirection.value.api
  );
  isLoading.value = false;
}

onBeforeMount(async () => {
  await loadColumn();
});

watchEffect(async () => {
  await loadColumn();
});
</script>

<template>
  <ul>
    <li v-for="timeslot in timeslots">
      <span v-if="isLoading" class="loading loading-spinner w-4 h-4"></span>
      <div
        v-else
        class="tooltip w-4 h-4 rounded-sm"
        :class="isAvailableForBooking(timeslot) ? 'bg-success' : 'bg-neutral'"
        :style="
          isAvailableForBooking(timeslot)
            ? `--tw-bg-opacity: ${getOpacity(timeslot)}`
            : ''
        "
        :data-tip="getTooltipText(timeslot)"
      ></div>
    </li>
  </ul>
</template>

<style scoped></style>
