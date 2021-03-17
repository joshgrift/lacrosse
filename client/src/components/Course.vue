<template>
  <div class="bg-gray-100 mt-5 p-3 px-4">
    <div class="grid grid-cols-2 grid-rows-2">
      <div>{{ course.code }} - {{ course.name }} ({{ course.term }})</div>
      <div class="text-right text-sm text-gray-500">
        <span
          class="block float-right w-6 h-6 mx-1 bg-green-100 rounded-full p-1"
          ><svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M5.636 18.364a9 9 0 010-12.728m12.728 0a9 9 0 010 12.728m-9.9-2.829a5 5 0 010-7.07m7.072 0a5 5 0 010 7.07M13 12a1 1 0 11-2 0 1 1 0 012 0z"
            /></svg
        ></span>
        <span
          class="block float-right w-6 h-6 mx-1 bg-green-100 rounded-full p-1"
          ><svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M8 14v3m4-3v3m4-3v3M3 21h18M3 10h18M3 7l9-4 9 4M4 10h16v11H4V10z"
            /></svg
        ></span>
      </div>
      <div class="text-sm text-gray-500">8:00am - 8:30am | MWF | N10001</div>
      <div class="text-sm text-gray-500 text-right">Prof. Martin</div>
    </div>

    <p class="mt-1 text-sm text-gray-700">
      Selected topics may include graph colouring, extremal graph theory, planar
      graphs, random graphs, network flows, algebraic methods in graph theory,
      Ramsay theory for graphs, matching theory, graph algorithms; application
      of graph theory, such as applications to scheduling, VLSI circuits,
      compiler design, computer vision and the design of internet search
      engines.
    </p>

    <p class="text-right text-xs mt-1 text-gray-400">
      <span class="text-yellow-500"> 5 seats remaining </span>| 0.5 credits
    </p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { Course } from "@/types";

export default defineComponent({
  props: {
    course: Object as () => Course,
  },
});
</script>

<style scoped lang="scss"></style>
