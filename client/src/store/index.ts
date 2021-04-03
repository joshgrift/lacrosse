import { Campus, Course, Department, Professor, Room, Semester } from "@/types";
import { createStore } from "vuex";
import { State } from "@vue/runtime-core";

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
    loadSearchParams(context) {
      const result = {
        professors: [
          {
            id: 0,
            name: "Prof. Martin",
          },
          {
            id: 1,
            name: "David Brown",
          },
        ],
        semesters: [
          {
            id: 1,
            name: "Fall 2020",
          },
        ],
        rooms: [
          {
            id: 0,
            name: "N10001",
            campus: 0,
          },
          {
            id: 1,
            name: "N10002",
            campus: 0,
          },
        ],
        campus: [
          {
            id: 0,
            name: "Waterloo",
          },
        ],
        departments: [
          {
            id: 0,
            name: "Computer Science",
            code: "CP",
          },
        ],
      };

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
    refreshCourses(context, query: string) {
      // TODO: query server
      console.log(query);

      const result = [
        {
          code: "CP102",
          id: 0,
          title: "Intro to Compsci",
          description: "Welcome to compsci",
          time_start: 17093949,
          time_end: 182748394,
          online: true,
          in_person: false,
          credits: 0.5,
          capacity: 150,
          space_left: 0,
          professor: 0,
          room: 0,
          semester: 0,
        },
      ];

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
