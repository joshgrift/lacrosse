import { Course } from "@/types";
import { createStore } from "vuex";

export default createStore({
  state: {
    courses: [
      {
        code: "CP465",
        name: "Databases",
        room: "N10001",
        term: "Winter",
      },
      {
        code: "CP418",
        name: "Something Else",
        room: "N10002",
        term: "Fall",
      },
    ],
  },
  mutations: {
    addCourse(state, course: Course) {
      state.courses.push(course);
    },
    removeCourses(state) {
      state.courses = [];
    },
  },
  actions: {
    refreshCourses(context, query: string) {
      // TODO: FETCH FROM SERVER AND UPDATE HERE
      console.log(query);
      context.commit("addCourse", {
        code: "CP418",
        name: "Something Else",
        room: "N10002",
        term: "Fall",
      });
    },
    clearCourses(context) {
      context.commit("removeCourses");
    },
  },
  modules: {},
});
