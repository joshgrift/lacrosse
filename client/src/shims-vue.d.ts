/* eslint-disable */
import { ComponentCustomProperties } from "vue";
import { Store } from "vuex";
import { Course, Department, Professor, Room, Semester } from "@/types";

declare module "*.vue" {
  import type { DefineComponent } from "vue";
  const component: DefineComponent<{}, {}, any>;
  export default component;
}

declare module "@vue/runtime-core" {
  // declare your own store states
  interface State {
    courses: Course[];
    professors: Professor[];
    campus: Campus[];
    semesters: Semester[];
    rooms: Room[];
    departments: Department[];
  }

  // provide typings for `this.$store`
  interface ComponentCustomProperties {
    $store: Store<State>;
  }
}
