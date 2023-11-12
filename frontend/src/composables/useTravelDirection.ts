import { Ref, ref } from "vue";

export const TRAVEL_DIRECTIONS = {
  sgToJb: { api: "sg-to-jb", display: "Sg to JB" },
  jbToSg: { api: "jb-to-sg", display: "JB to Sg" },
};

interface TravelDirection {
  api: string;
  display: string;
}

export function useTravelDirection() {
  const currentTravelDirection: Ref<TravelDirection> = ref(
    TRAVEL_DIRECTIONS.sgToJb
  );

  function setTravelDirection(travelDirection: TravelDirection) {
    currentTravelDirection.value = travelDirection;
  }

  return { currentTravelDirection, setTravelDirection };
}
