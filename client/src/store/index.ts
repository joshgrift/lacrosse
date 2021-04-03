import { Campus, Course, Department, Professor, Room, Semester } from "@/types";
import { createStore } from "vuex";
import { State } from "@vue/runtime-core";

const URL = "http://localhost:8000";

export default createStore({
  state: {
    courses: [],
    professors: [],
    semesters: [],
    rooms: [],
    campus: [],
    departments: [],
  } as State,
  mutations: {
    addCourse(state, course: Course) {
      state.courses.push(course);
    },
    removeCourses(state) {
      state.courses = [];
    },
    addProfessor(state, p: Professor) {
      state.professors.push(p);
    },
    addSemester(state, p: Semester) {
      state.semesters.push(p);
    },
    addRoom(state, p: Room) {
      state.rooms.push(p);
    },
    addCampus(state, p: Campus) {
      state.campus.push(p);
    },
    addDepartment(state, p: Department) {
      state.departments.push(p);
    },
  },
  actions: {
    async loadSearchParams(context) {
      type searchParamsServerReturn = {
        professors: {
          id: number;
          name: string;
        }[];
        campus: {
          id: number;
          name: string;
        }[];
        semesters: {
          id: number;
          name: string;
        }[];
        rooms: {
          id: number;
          name: string;
          campus: number;
        }[];
        departments: {
          id: number;
          name: string;
          code: string;
        }[];
      };

      const response = await fetch(URL + "/search-params");
      const result = (await response.json()) as searchParamsServerReturn;

      result.professors.forEach((p) => {
        context.commit("addProfessor", p);
      });

      result.semesters.forEach((p) => {
        context.commit("addSemester", p);
      });

      result.campus.forEach((p) => {
        context.commit("addCampus", p);
      });

      result.departments.forEach((p) => {
        context.commit("addDepartment", p);
      });

      result.rooms.forEach((p) => {
        const key = p.campus;
        p.campus = context.state.campus[key];
        context.commit("addRoom", p);
      });
    },
    async refreshCourses(context, query: string) {
      context.commit("removeCourses");
      type courseQueryResult = {
        id: number;
        code: string;
        title: string;
        description: string;
        time_start: number;
        time_end: number;
        online: boolean;
        in_person: boolean;
        credits: number;
        capacity: number;
        space_left: number;
        professor: number;
        room: number;
        semester: number;
      }[];

      const response = await fetch(URL + "/query" + query);
      const result = (await response.json()).courses as courseQueryResult;

      result.forEach((c) => {
        const course: Course = {
          code: c.code,
          id: c.id,
          title: c.title,
          description: c.description,
          time_start: c.time_end,
          time_end: c.time_start,
          online: c.online,
          in_person: c.in_person,
          credits: c.credits,
          capacity: c.capacity,
          space_left: c.space_left,
          room: context.state.rooms[c.room],
          professor: context.state.professors[c.professor],
          semester: context.state.semesters[c.semester],
        };

        context.commit("addCourse", course);
      });
    },
    clearCourses(context) {
      context.commit("removeCourses");
    },
  },
  modules: {},
});
