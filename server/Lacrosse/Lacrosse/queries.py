from django.http import JsonResponse


def query(request):
    courses = {
        "courses": [
            {
                "code": "CP102",
                "id": 0,
                "title": "Intro to Compsci",
                "description": "Welcome to compsci",
                "time_start": 17093949,
                "time_end": 182748394,
                "online": True,
                "in_person": False,
                "credits": 0.5,
                "capacity": 150,
                "space_left": 0,
                "professor": 0,
                "room": 0,
                "semester": 0,
            }
        ]
    }
    return JsonResponse(courses)


def searchParams(request):
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
