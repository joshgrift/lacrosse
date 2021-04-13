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
              name="course"
            />
          </div>

          <div class="mt-4">
            <label class="block text-sm" for="professor">Professor</label>
            <select
              class="box-border w-full mt-1 block rounded-sm p-2 text-black"
              id="professor"
              name="professor"
            >
              <option value="null" selected>Any</option>
              <option
                v-for="professor in professors"
                v-bind:key="professor.id"
                v-bind:value="professor.id"
              >
                {{ professor.name }}
              </option>
            </select>
          </div>

          <div class="mt-4">
            <label class="block text-sm" for="semester">Semester</label>
            <select
              class="box-border w-full mt-1 block rounded-sm p-2 text-black"
              id="professor"
              name="professor"
            >
              <option value="null" selected>Any</option>
              <option
                v-for="semester in semesters"
                v-bind:key="semester.id"
                v-bind:value="semester.id"
              >
                {{ semester.name }}
              </option>
            </select>
          </div>

          <div class="mt-4">
            <label class="block text-sm" for="department">Department</label>
            <select
              class="box-border w-full mt-1 block rounded-sm p-2 text-black"
              id="department"
              name="department"
            >
              <option value="null" selected>Any</option>
              <option
                v-for="department in departments"
                v-bind:key="department.id"
                v-bind:value="department.id"
              >
                {{ department.code }} - {{ department.name }}
              </option>
            </select>
          </div>

          <div class="mt-4">
            <label class="block text-sm" for="room">Room</label>
            <select
              class="box-border w-full mt-1 block rounded-sm p-2 text-black"
              id="room"
              name="room"
            >
              <option value="null" selected>Any</option>
              <option
                v-for="room in rooms"
                v-bind:key="room.id"
                v-bind:value="room.id"
              >
                {{ room.name }} - {{ room.campus.name }}
              </option>
            </select>
          </div>

          <div class="mt-4">
            <label class="block text-sm" for="online">Online</label>
            <select
              class="box-border w-full mt-1 block rounded-sm p-2 text-black"
              id="online"
              name="online"
            >
              <option value="null" selected>Any</option>
              <option value="1">Yes</option>
              <option value="0">No</option>
            </select>
          </div>

          <div class="mt-4">
            <label class="block text-sm" for="in_person">In Person</label>
            <select
              class="box-border w-full mt-1 block rounded-sm p-2 text-black"
              id="in_person"
              name="in_person"
            >
              <option value="null" selected>Any</option>
              <option value="1">Yes</option>
              <option value="0">No</option>
            </select>
          </div>

          <div class="mt-4">
            <label class="block text-sm" for="credits">Credits</label>
            <select
              class="box-border w-full mt-1 block rounded-sm p-2 text-black"
              id="credits"
              name="credits"
            >
              <option value="null" selected>Any</option>
              <option value="0.5">0.5</option>
              <option value="1">1</option>
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
import {
  Campus,
  Course as CourseType,
  Department,
  Professor,
  Room,
  Semester,
} from "@/types";

export default defineComponent({
  components: {
    Course,
  },
  computed: {
    courses(): CourseType[] {
      return this.$store.state.courses;
    },
    professors(): Professor[] {
      return this.$store.state.professors;
    },
    semesters(): Semester[] {
      return this.$store.state.semesters;
    },
    campus(): Campus[] {
      return this.$store.state.campus;
    },
    departments(): Department[] {
      return this.$store.state.departments;
    },
    rooms(): Room[] {
      return this.$store.state.rooms;
    },
  },
  methods: {
    refresh(e: InputEvent) {
      if (e.currentTarget) {
        let target = e.currentTarget as HTMLElement;
        let params = "?limit=100";

        target.querySelectorAll("input").forEach((e) => {
          if (e.value) {
            params += `&${e.name}=${e.value}`;
          }
        });

        target.querySelectorAll("select").forEach((e) => {
          if (e.value && e.value != "null") {
            params += `&${e.name}=${e.value}`;
          }
        });

        this.$store.dispatch("refreshCourses", params);
      }
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