<script setup lang="ts">
import { useTicketAvailability } from "@/composables/useTicketAvailability";
import { Ref, onBeforeMount, ref, watchEffect } from "vue";

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

async function loadPage() {
  isLoading.value = true;
  await createTicketAvailabilityResponse(props.date);
  isLoading.value = false;
}

onBeforeMount(async () => {
  await loadPage();
});

watchEffect(async () => {
  await loadPage();
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
        :data-tip="getTooltipText(timeslot)"
      ></div>
    </li>
  </ul>
</template>

<style scoped></style>
