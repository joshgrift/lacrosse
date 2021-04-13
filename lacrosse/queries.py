from django.http import JsonResponse
import mysql.connector


def query(request):
    print(request.GET["limit"])
    mydb = mysql.connector.connect(
        host="db-mysql-tor1-86354-do-user-3862566-0.b.db.ondigitalocean.com",
        user="cp465",
        password="fskjd3njkfds8jk3ASDFuq38",
        database="cp465",
        port="25060"
    )
    cursor = mydb.cursor()
    userQuery = "SELECT code, id, title, description, online, in_person, credits, capacity, professor, semester, room FROM course WHERE 1 = 1 "
    if "professor" in request.GET:
        userQuery += " AND professor = " + request.GET.get("professor", False)
    if "semester" in request.GET:
        userQuery += " AND semester = " + request.GET.get("semester", False)
    if "department" in request.GET:
        userQuery += " AND department = " + \
            request.GET.get("department", False)
    if "room" in request.GET:
        userQuery += " AND room = " + request.GET.get("room", False)
    if "course" in request.GET:
        userQuery += " AND code LIKE '%" + \
            request.GET.get("course", False) + "%'"
    if "online" in request.GET:
        userQuery += " AND online = " + request.GET.get("online", False)
    if "in_person" in request.GET:
        userQuery += " AND in_person = " + request.GET.get("in_person", False)
    if "credits" in request.GET:
        userQuery += " AND credits = " + request.GET.get("credits", False)

    userQuery += " LIMIT " + request.GET.get("limit", False)
    cursor.execute(userQuery)
    result = cursor.fetchall()

    courses = []
    for obj in result:
        courses.append({
            "code": obj[0],
            "id": obj[1],
            "title": obj[2],
            "description": obj[3],
            "online": obj[4],
            "in_person": obj[5],
            "credits": obj[6],
            "capacity": obj[7],
            "professor": obj[8],
            "semester": obj[9],
            "room": obj[10],
            "time_start": 0,
            "time_end": 0
        })

    return JsonResponse(courses, safe=False)


def searchParams(request):
    mydb = mysql.connector.connect(
        host="db-mysql-tor1-86354-do-user-3862566-0.b.db.ondigitalocean.com",
        user="cp465",
        password="fskjd3njkfds8jk3ASDFuq38",
        database="cp465",
        port=25060
    )

    # --------- PROFESSOR ---------
    cursor1 = mydb.cursor()

    professorQuery = "SELECT * FROM professor"
    cursor1.execute(professorQuery)

    result1 = cursor1.fetchall()

    prof_list = []
    for obj in result1:
        prof_list.append({
            "id": obj[0],
            "name": obj[1],
        })

    # --------- DEPARTMENT ---------
    cursor2 = mydb.cursor()

    departmentQuery = "SELECT * FROM department"
    cursor2.execute(departmentQuery)

    result2 = cursor2.fetchall()

    department_list = []
    for obj in result2:
        department_list.append({
            "id": obj[0],
            "name": obj[1],
            "code": obj[2]
        })

    # --------- SEMESTER ---------
    cursor3 = mydb.cursor()

    semesterQuery = "SELECT * FROM semester"
    cursor3.execute(semesterQuery)

    result3 = cursor3.fetchall()

    semester_list = []
    for obj in result3:
        semester_list.append({
            "id": obj[0],
            "name": obj[1]
        })

    # --------- ROOMS ---------
    cursor4 = mydb.cursor()

    semesterQuery = "SELECT * FROM room"
    cursor4.execute(semesterQuery)

    result4 = cursor4.fetchall()

    room_list = []
    for obj in result4:
        room_list.append({
            "id": obj[0],
            "campus": obj[1],
            "name": obj[2],
        })
    # --------- CAMPUS ---------
    cursor5 = mydb.cursor()

    campusQuery = "SELECT * FROM campus"

    cursor5.execute(campusQuery)
    result5 = cursor5.fetchall()

    campus_list = []
    for obj in cursor5:
        campus_list.append({
            "id": obj[0],
            "name": obj[1]
        })

    params = {
        "professors": prof_list,
        "semesters": semester_list,
        "rooms": room_list,
        "campus": campus_list,
        "departments": department_list
    }
    return JsonResponse(params)
