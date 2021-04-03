from django.http import HttpResponse


def hello_world(request):
    test = "Hello! Use /query or /searchParams"
    return HttpResponse(test)
