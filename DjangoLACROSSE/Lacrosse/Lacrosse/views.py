from django.http import HttpResponse

def hello_world(request):
    test = "Hello World"
    return HttpResponse(test)