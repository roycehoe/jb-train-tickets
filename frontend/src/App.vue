<script setup lang="ts">
import AvailabilityIndicator from "@/components/availability-indicator/Index.vue";
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
      </div>
    </div>
  </div>
</template>
<style scoped></style>
