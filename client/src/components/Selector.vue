<template>
  <label class="block text-sm" for="semester">Semester</label>
  <select
    class="box-border w-full mt-1 block rounded-sm p-2 text-black"
    id="professor"
    name="professor"
  >
    <option
      v-for="professor in professors"
      v-bind:key="professor.id"
      v-bind:value="professor.id"
    >
      {{ professor.name }}
    </option>
  </select>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { Course } from "@/types";

type List = [
  {
    id: number;
    text: string;
  }
];

export default defineComponent({
  props: {
    objects: Object as () => Course,
  },
});
</script>

<style scoped lang="scss"></style>
