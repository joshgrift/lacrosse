from django.http import JsonResponse
#import mysql.connector


def query(request):
    print(request.GET["limit"])
    #mydb = mysql.connector.connect(
    #    host = "db-mysql-tor1-86354-do-user-3862566-0.b.db.ondigitalocean.com:25060",
    #    user = "cp465",
    #    password = "fskjd3njkfds8jk3ASDFuq38",
    #    database = "cp465"
    #)
    #cursor = mydb.cursor()
    userQuery = "SELECT * FROM course WHERE"
    if "limit" in request.GET:
        userQuery += " limit = " + request.GET.get("limit", False)
    if "professor" in request.GET:
        userQuery += " AND professor = " + request.GET.get("professor", False)
    if "semester" in request.GET:
        userQuery += " AND semester = " + request.GET.get("semester", False)
    if "department" in request.GET:
        userQuery += " AND department = " + request.GET.get("department", False)
    if "room" in request.GET:
        userQuery += " AND room = " + request.GET("room", False)
    if "course" in request.GET:
        userQuery += " AND course = " + request.GET("course", False)
    if "online" in request.GET:
        userQuery += " AND online = " + request.GET("online", False)
    if "in_person" in request:
        userQuery += " AND in_person = " + request.GET("in_person", False)
    if "credits" in request:
        userQuery += " AND credits = " + request.GET("credits", False)
    print(userQuery)
    #cursor.execute(userQuery)
    #result = cursor.fetchall()

    courses = {

    }

    #courses = {
    #    "courses": [
    #        {
    #            "code": "CP102",
    #            "id": 0,
    #            "title": "Intro to Compsci",
    #            "description": "Welcome to compsci",
    #            "time_start": 17093949,
    #            "time_end": 182748394,
    #            "online": True,
    #            "in_person": False,
    #            "credits": 0.5,
    #            "capacity": 150,
    #            "space_left": 0,
    #            "professor": 0,
    #            "room": 0,
    #            "semester": 0,
    #        }
    #    ]
    #}
    return JsonResponse(courses)


def searchParams(request):
    # rooms semesters + campus are not used
    # need query for professors and department
    #mydb = mysql.connector.connect(
    #    host="db-mysql-tor1-86354-do-user-3862566-0.b.db.ondigitalocean.com:25060",
    #    user="cp465",
    #    password="fskjd3njkfds8jk3ASDFuq38",
    #    database="cp465"
    #)

    # --------- PROFESSOR ---------
    # cursor1 = mydb.cursor()

    professorQuery = "SELECT * FROM professor"
    # cursor1.execute(professorQuery)

    # result1 = cursor1.fetchall()

    # --------- DEPARTMENT ---------
    # cursor2 = mydb.cursor()

    departmentQuery = "SELECT * FROM department"
    # cursor2.execute(departmentQuery)

    # result2 = cursor2.fetchall()

    # --------- SEMESTER ---------
    # cursor3 = mydb.cursor()

    # semesterQuery = "SELECT * FROM semester"
    # cursor3.execute(semesterQuery)

    # result3 = cursor3.fetchall()

    # --------- ROOMS ---------
    # cursor4 = mydb.cursor()

    # semesterQuery = "SELECT * FROM semester"
    # cursor4.execute(semesterQuery)

    # result4 = cursor4.fetchall()

    # --------- CAMPUS ---------
    # cursor5 = mydb.cursor()

    # semesterQuery = "SELECT * FROM semester"

    # cursor5.execute(semesterQuery)
    # result5 = cursor5.fetchall()

    params = {
        "professors": [
            {
                "id": 0,
                "name": "Prof. Martin",
            },
            {
                "id": 1,
                "name": "David Brown",
            },
        ],
        "semesters": [
            {
                "id": 1,
                "name": "Fall 2020",
            },
        ],
        "rooms": [
            {
                "id": 0,
                "name": "N10001",
                "campus": 0,
            },
            {
                "id": 1,
                "name": "N10002",
                "campus": 0,
            },
        ],
        "campus": [
            {
                "id": 0,
                "name": "Waterloo",
            },
        ],
        "departments": [
            {
                "id": 0,
                "name": "Computer Science",
                "code": "CP",
            },
        ]
    }
    return JsonResponse(params)
