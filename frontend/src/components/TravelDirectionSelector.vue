<script setup lang="ts">
import {
  TRAVEL_DIRECTIONS,
  currentTravelDirection,
  useTravelDirection,
} from "@/composables/useTravelDirection";

const { setTravelDirection } = useTravelDirection();
</script>

<template>
  <div class="tabs tabs-boxed">
    <a
      class="tab"
      :class="
        travelDirection.api === currentTravelDirection.api ? `tab-active` : ''
      "
      v-for="travelDirection in TRAVEL_DIRECTIONS"
      @click="setTravelDirection(travelDirection)"
      >{{ travelDirection.display }}</a
    >
  </div>
</template>

<style scoped></style>
