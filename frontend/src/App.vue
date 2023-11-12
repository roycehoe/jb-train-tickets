<script setup lang="ts">
// import from "@/components/availability-indicator/Index.vue";
import AvailabilityTable from "@/components/AvailabilityTable.vue";
import MonthSelector from "./components/MonthSelector.vue";
import TravelDirectionSelector from "./components/TravelDirectionSelector.vue";
MonthSelector;
</script>

<template>
  <div class="w-screen h-screen flex flex-col">
    <div class="flex justify-center items-center mt-16 flex-col">
      <div class="flex gap-4 flex-col">
        <div class="flex flex-col justify-center items-center m-8">
          <MonthSelector></MonthSelector>
        </div>
        <AvailabilityTable></AvailabilityTable>
        <div class="flex">
          <TravelDirectionSelector></TravelDirectionSelector>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped></style>
