<script setup lang="ts">
// import from "@/components/availability-indicator/Index.vue";
import AvailabilityTable from "@/components/AvailabilityTable.vue";
import MonthSelector from "./components/MonthSelector.vue";
import TravelDirectionSelector from "./components/TravelDirectionSelector.vue";
MonthSelector;
</script>

<template>
  <div class="w-screen h-screen flex flex-col">
    <div class="flex justify-center items-center mt-16">
      <!-- <div>
        <div class="flex justify-center items-center m-16">
          <MonthSelector></MonthSelector>
        </div>
        <div class="flex justify-center items-center m-16">
          <TravelDirectionSelector></TravelDirectionSelector>
        </div>
        <AvailabilityTable></AvailabilityTable>
      </div> -->
      <div>
        <div class="flex flex-col justify-center items-center m-16 gap-16">
          <MonthSelector></MonthSelector>
          <TravelDirectionSelector></TravelDirectionSelector>
        </div>
        <AvailabilityTable></AvailabilityTable>
      </div>
    </div>
  </div>
</template>
<style scoped></style>
