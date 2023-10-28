<script setup lang="ts">
import { onBeforeMount } from "vue";
import { useDate } from "../../composables/useDate";
import DayAvailabilityIndicator from "./DayAvailabilityIndicator.vue";
const { datesInMonth, setDatesInMonth } = useDate();

const TRAIN_TIMESLOTS = [
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
  "22:45",
];

const DAY_TO_DAY_TEXT_MAP: { [key: number]: string } = {
  0: "Su",
  1: "Mo",
  2: "Tu",
  3: "We",
  4: "Th",
  5: "Fr",
  6: "Sa",
};

onBeforeMount(() => {
  setDatesInMonth();
});
</script>

<template>
  <table class="table table-xs">
    <thead>
      <tr class="border-b-0">
        <th></th>
        <th v-for="date in datesInMonth">
          <p class="text-center" :class="date.getDay() === 0 && 'ml-2'">
            {{ DAY_TO_DAY_TEXT_MAP[date.getDay()] }}
          </p>
        </th>
      </tr>
      <tr class="border-b-0">
        <th></th>
        <th v-for="date in datesInMonth">
          <p class="text-center" :class="date.getDay() === 0 && 'ml-2'">
            {{ date.getDate() }}
          </p>
        </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td></td>
        <td v-for="date in datesInMonth">
          <DayAvailabilityIndicator
            :class="date.getDay() === 0 && 'ml-2'"
            :date="date"
            :timeslots="TRAIN_TIMESLOTS"
          ></DayAvailabilityIndicator>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped></style>
