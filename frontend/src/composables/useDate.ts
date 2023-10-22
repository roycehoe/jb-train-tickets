import { Ref, ref } from "vue";

const currentDate: Ref<Date> = ref(new Date());
const datesInMonth: Ref<Date[]> = ref([]);

export function useDate() {
  function incrementCurrentMonth() {
    currentDate.value = new Date(
      currentDate.value.setMonth(currentDate.value.getMonth() + 1)
    );
    setDatesInMonth();
  }

  function decrementCurrentMonth() {
    currentDate.value = new Date(
      currentDate.value.setMonth(currentDate.value.getMonth() - 1)
    );
    setDatesInMonth();
  }

  function displayDate() {
    return currentDate.value.toLocaleString("en-US", {
      year: "numeric",
      month: "long",
    });
  }

  function setDatesInMonth(): void {
    const year = currentDate.value.getFullYear();
    const month = currentDate.value.getMonth();
    const days: Date[] = [];

    const date: Date = new Date(year, month, 1);
    while (date.getMonth() === month) {
      days.push(new Date(date));
      date.setDate(date.getDate() + 1);
    }
    datesInMonth.value = days;
  }

  return {
    currentDate,
    datesInMonth,
    displayDate,
    incrementCurrentMonth,
    decrementCurrentMonth,
    setDatesInMonth,
  };
}
