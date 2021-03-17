<template>
  <div class="container mx-auto">
    <div class="md:grid grid-cols-3 gap-4">
      <div class="bg-indigo-900 text-white p-4 w-64">
        <h1 class="mb-2">Lacrosse</h1>

        <form @input="refresh($event)">
          <div class="mt-4">
            <label class="block text-sm" for="course">Course</label>
            <input
              class="box-border w-full block mt-1 rounded-sm p-2 text-black"
              type="text"
              id="course"
            />
          </div>

          <div class="mt-4">
            <label class="block text-sm" for="professor">Professor</label>
            <select
              class="box-border w-full mt-1 block rounded-sm p-2 text-black"
              id="professor"
            >
              <option>United States</option>
              <option>Canada</option>
              <option>Mexico</option>
            </select>
          </div>
        </form>
      </div>
      <div class="col-span-2 p-8">
        <Course
          v-for="course in courses"
          v-bind:key="course.code"
          :course="course"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Course from "@/components/Course.vue";
import { Course as CourseType } from "@/types";

export default defineComponent({
  components: {
    Course,
  },
  computed: {
    courses(): CourseType[] {
      return this.$store.state.courses;
    },
  },
  methods: {
    refresh(e: InputEvent) {
      console.log(e.data);
      let target = e.target;
      let query = "?limit=100";

      this.$store.dispatch("refreshCourses", query);
    },
    clear() {
      this.$store.dispatch("clearCourses");
    },
  },
});
</script>

<style lang="scss">
@tailwind base;
@tailwind components;
@tailwind utilities;
</style>
