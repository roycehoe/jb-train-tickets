<script setup lang="ts">
import { Err, Ok, Result } from "ts-results";
import { Ref, onBeforeMount, ref, watch } from "vue";
import { client } from "../../services";

export interface AtlasAvailabilityData {
  date: string;
  time: string;
  is_available: boolean;
  dining_type: string;
}

const props = defineProps<{
  date: Date;
  timeslots: string[];
}>();
const isLoading: Ref<boolean> = ref(false);
const availabilities: Ref<AtlasAvailabilityData[]> = ref([]);
const day: Ref<Date> = ref(props.date);
const timeslots: Ref<string[]> = ref(props.timeslots);
const noDataFromApi: Ref<boolean> = ref(false);

async function getAtlasAvailabilityResponse(
  date: string
): Promise<Result<AtlasAvailabilityData[], any>> {
  try {
    const response = await client.get(date);
    return Ok(response.data as AtlasAvailabilityData[]);
  } catch (error) {
    return Err(error);
  }
}

function getApiFormattedDate(date: Date): string {
  const day = date.getDate();
  const month = date.getMonth() + 1;
  const year = date.getFullYear();

  return `${day}-${month}-${year}`;
}
function isAvailableForDrinks(timeslot: string) {
  const timeslotData = availabilities.value
    .filter((availability) => {
      return availability.time === timeslot;
    })
    .filter((availability) => {
      return (
        availability.dining_type === "Drinks" ||
        availability.dining_type === "Cocktails"
      );
    });
  return timeslotData.length !== 0;
}

function isAvailableForNonDrinks(timeslot: string) {
  const timeslotData = availabilities.value
    .filter((availability) => {
      return availability.time === timeslot;
    })
    .filter((availability) => {
      return (
        availability.dining_type !== "Drinks" &&
        availability.dining_type !== "Cocktails" &&
        availability.dining_type !== "NA"
      );
    });
  return timeslotData.length !== 0;
}

async function loadPage() {
  isLoading.value = true;
  const apiFormattedDate = getApiFormattedDate(day.value);
  const response = await getAtlasAvailabilityResponse(apiFormattedDate);
  if (response.ok) {
    availabilities.value = response.val;
  } else {
    noDataFromApi.value = true;
  }
  isLoading.value = false;
}

onBeforeMount(async () => {
  await loadPage();
});

watch(props, async (newProps) => {
  day.value = newProps.date;
  noDataFromApi.value = false;
  await loadPage();
});
</script>

<template>
  <ul v-if="!noDataFromApi">
    <li v-for="timeslot in timeslots">
      <span v-if="isLoading" class="loading loading-spinner w-4 h-4"></span>
      <div
        v-else-if="isAvailableForDrinks(timeslot)"
        class="tooltip w-4 h-4 bg-success rounded-sm"
        :data-tip="timeslot"
      ></div>

      <div
        v-else-if="isAvailableForNonDrinks(timeslot)"
        class="tooltip w-4 h-4 bg-primary rounded-sm"
        :data-tip="timeslot"
      ></div>

      <div
        v-else
        class="tooltip w-4 h-4 bg-neutral rounded-sm"
        :data-tip="timeslot"
      ></div>
    </li>
  </ul>
</template>

<style scoped></style>
