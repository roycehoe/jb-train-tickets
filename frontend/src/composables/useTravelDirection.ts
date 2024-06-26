import { Ref, ref } from "vue";

export const TRAVEL_DIRECTIONS = {
  sgToJb: { api: "sg_to_jb", display: "Sg to JB" },
  jbToSg: { api: "jb_to_sg", display: "JB to Sg" },
};

interface TravelDirection {
  api: string;
  display: string;
}

export const currentTravelDirection: Ref<TravelDirection> = ref(
  TRAVEL_DIRECTIONS.sgToJb
);

export function useTravelDirection() {
  function setTravelDirection(travelDirection: TravelDirection) {
    currentTravelDirection.value = travelDirection;
  }

  return { setTravelDirection };
}
