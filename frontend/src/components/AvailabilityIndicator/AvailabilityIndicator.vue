<script setup lang="ts">
import { onBeforeMount } from "vue";
import { useDate } from "../../composables/useDate";
import DayAvailabilityIndicator from "./DayAvailabilityIndicator.vue";
const { datesInMonth, setDatesInMonth } = useDate();

const ATLAS_TIMESLOTS = [
  "05:00",
  "05:30",
  "06:00",
  "06:30",
  "07:00",
  "07:30",
  "08:45",
  "10:00",
  "11:30",
  "12:45",
  "14:00",
  "15:15",
  "16:30",
  "17:45",
  "19:00",
  "20:15",
  "21:30",
  "22:45"
]

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
