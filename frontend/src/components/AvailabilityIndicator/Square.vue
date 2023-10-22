<script setup lang="ts">
import { Ref, ref } from "vue";
import { AtlasAvailabilityData } from "./DayAvailabilityIndicator.vue";

const props = defineProps<{
  isLoading: boolean;
  content: string;
  isAvailableForDrinks: boolean;
  isAvailableForNonDrinks: boolean;
}>();

const atlasAvailabilityData: Ref<AtlasAvailabilityData> = ref(
  {} as AtlasAvailabilityData
);

const content: Ref<string> = ref(props.content);
const isLoading: Ref<boolean> = ref(props.isLoading);
const isAvailableForDrinks: Ref<boolean> = ref(props.isAvailableForDrinks);
const isAvailableForNonDrinks: Ref<boolean> = ref(
  props.isAvailableForNonDrinks
);
</script>

<template>
  <div
    v-if="isAvailableForDrinks"
    class="tooltip w-4 h-4 bg-success rounded-sm"
    data-tip="Tooltip data"
  ></div>

  <div
    v-else-if="isAvailableForNonDrinks"
    class="tooltip w-4 h-4 bg-primary rounded-sm"
    data-tip="Tooltip data"
  ></div>

  <div
    v-else
    class="tooltip w-4 h-4 bg-neutral rounded-sm"
    data-tip="Tooltip data"
  ></div>
</template>

<style scoped></style>
