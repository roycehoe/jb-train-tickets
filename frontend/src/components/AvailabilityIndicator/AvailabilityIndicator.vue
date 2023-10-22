<script setup lang="ts">
import { onBeforeMount } from "vue";
import { useDate } from "../../composables/useDate";
import DayAvailabilityIndicator from "./DayAvailabilityIndicator.vue";
const { datesInMonth, setDatesInMonth } = useDate();

const ATLAS_TIMESLOTS = [
  "12:00",
  "12:30",
  "13:00",
  "13:30",
  "14:00",
  "14:30",
  "15:00",
  "15:30",
  "16:00",
  "16:30",
  "17:00",
  "17:30",
  "18:00",
  "18:30",
  "19:00",
  "19:30",
  "20:00",
  "20:30",
  "21:00",
  "21:30",
  "22:00",
];

onBeforeMount(() => {
  setDatesInMonth();
});
</script>

<template>
  <table class="table table-xs">
    <thead>
      <tr>
        <th></th>
        <th v-for="date in datesInMonth">
          <p class="text-center">{{ date.getDate() }}</p>
        </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td></td>
        <td v-for="date in datesInMonth">
          <DayAvailabilityIndicator
            :date="date"
            :timeslots="ATLAS_TIMESLOTS"
          ></DayAvailabilityIndicator>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped></style>
