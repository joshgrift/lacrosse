export type Course = {
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

  /**
   * @deprecated
   */
  space_left: number;

  professor: Professor;
  room: Room;
  semester: Semester;
};

export type Professor = IdName;
export type Semester = IdName;
export type Campus = IdName;

export type Room = {
  id: number;
  campus: Campus;
  name: string;
};

export type Department = {
  id: number;
  name: string;
  code: string;
};

type IdName = {
  id: number;
  name: string;
};
