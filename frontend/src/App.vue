<script setup lang="ts">
import AvailabilityIndicator from "./components/AvailabilityIndicator/AvailabilityIndicator.vue";
import MonthSelector from "./components/MonthSelector.vue";
MonthSelector;
</script>

<template>
  <div class="w-screen h-screen flex flex-col">
    <div class="flex justify-center items-center mt-16">
      <div>
        <div class="flex justify-center items-center m-16">
          <MonthSelector></MonthSelector>
        </div>
        <AvailabilityIndicator></AvailabilityIndicator>
        <div class="my-12">
          <div class="flex gap-4 items-center">
            <div class="tooltip w-4 h-4 bg-success rounded-sm"></div>
            <p>-</p>
            <p>Drinks</p>
          </div>
          <div class="flex gap-4 items-center">
            <div class="tooltip w-4 h-4 bg-primary rounded-sm"></div>
            <p>-</p>
            <p>Food</p>
          </div>
          <div class="flex gap-4 items-center">
            <div class="tooltip w-4 h-4 bg-neutral rounded-sm"></div>
            <p>-</p>
            <p>Unavailable</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped></style>
